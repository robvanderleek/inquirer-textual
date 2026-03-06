from __future__ import annotations

from functools import partial
from typing import Optional, Any, Callable

from inquirer_textual.common.Choice import Choice


def _rank_task(scorer: Callable[[str, str], tuple[float, Optional[list[int]]]], needle: str, haystacks: list[str]) -> \
        list[dict[str, Any]]:
    result = []
    for haystack in haystacks:
        score, indices = scorer(needle, haystack)
        if indices is None:
            continue
        result.append({"score": score, "indices": indices, "haystack": haystack})
    result.sort(key=lambda x: x["score"], reverse=True)
    return result


def fuzzy_match(needle: str, haystacks: list[str]) -> list[dict[str, Any]]:
    results = _rank_task(_fzy_scorer, needle, haystacks)
    return [{"value": candidate["haystack"], "indices": candidate["indices"]} for candidate in results]


def substr_match(key: str, entries: list[str | Choice]) -> list[dict[str, Any]]:
    results = _rank_task(_substr_scorer, key, entries)
    return [{"value": res["haystack"], "indices": res["indices"]} for res in results]


SCORE_MIN = float("-inf")
SCORE_MAX = float("inf")
SCORE_GAP_LEADING = -0.005
SCORE_GAP_TRAILING = -0.005
SCORE_GAP_INNER = -0.01
SCORE_MATCH_CONSECUTIVE = 1.0


def _char_range_with(char_start: str, char_stop: str, value, hash_table: dict[str, int | float]) -> dict[
    str, int | float]:
    hash_table = hash_table.copy()
    hash_table.update(
        (chr(uni_char), value)
        for uni_char in range(ord(char_start), ord(char_stop) + 1)
    )
    return hash_table


lower_with = partial(_char_range_with, "a", "z")
upper_with = partial(_char_range_with, "A", "Z")
digit_with = partial(_char_range_with, "0", "9")

SCORE_MATCH_SLASH = 0.9
SCORE_MATCH_WORD = 0.8
SCORE_MATCH_CAPITAL = 0.7
SCORE_MATCH_DOT = 0.6
BONUS_MAP = {
    "/": SCORE_MATCH_SLASH,
    "-": SCORE_MATCH_WORD,
    "_": SCORE_MATCH_WORD,
    " ": SCORE_MATCH_WORD,
    ".": SCORE_MATCH_DOT,
}
BONUS_STATES = [{}, BONUS_MAP, lower_with(SCORE_MATCH_CAPITAL, BONUS_MAP)]
BONUS_INDEX = digit_with(1, lower_with(1, upper_with(2, {})))


def _bonus(haystack: str) -> list[float]:
    prev_char = "/"
    bonus = []
    for char in haystack:
        bonus.append(BONUS_STATES[BONUS_INDEX.get(char, 0)].get(prev_char, 0))
        prev_char = char
    return bonus


def _score(needle: str, haystack: str) -> tuple[float, Optional[list[int]]]:
    """Use fzy logic to calculate score for `needle` within the given `haystack`.

    2 2D array to track the score.
    1. The running score (`running_score`) which represents the best score for the current position.
    2. The result score (`result_score`) which tracks to overall best score that could be for the current positon.

    With every consequtive match, additional bonuse score are given and for every non matching char, a negative
    gap score is applied.

    After the score is calculated, the final matching score will be stored at the last position of the `result_score`.

    Backtrack the result by comparing the 2 2D array to find the corresponding indices.

    Args:
        needle: Substring to find in haystack.
        haystack: String to be searched and scored.

    Returns:
        A tuple of matching score with a list of matching indices.
    """
    needle_len, haystack_len = len(needle), len(haystack)
    bonus_score = _bonus(haystack)

    # smart case
    if needle.islower():
        haystack = haystack.lower()

    # return all values if no query
    if needle_len == 0 or needle_len == haystack_len:
        return SCORE_MAX, list(range(needle_len))

    # best score for the position
    running_score: list[list[float]] = [
        [0 for _ in range(haystack_len)] for _ in range(needle_len)
    ]

    # overall best score at each position
    result_score: list[list[float]] = [
        [0 for _ in range(haystack_len)] for _ in range(needle_len)
    ]

    for i in range(needle_len):
        prev_score = SCORE_MIN

        # gap between matching char
        # more gaps, less score
        gap_score = SCORE_GAP_TRAILING if i == needle_len - 1 else SCORE_GAP_INNER

        for j in range(haystack_len):
            if needle[i] == haystack[j]:
                score = SCORE_MIN
                if i == 0:
                    score = j * SCORE_GAP_LEADING + bonus_score[j]
                elif j != 0:
                    score = max(
                        result_score[i - 1][j - 1] + bonus_score[j],
                        # consecutive match if value is higher
                        running_score[i - 1][j - 1] + SCORE_MATCH_CONSECUTIVE,
                    )
                running_score[i][j] = score
                result_score[i][j] = prev_score = max(score, prev_score + gap_score)
            else:
                running_score[i][j] = SCORE_MIN
                # increment the best score with gap_score since no match
                result_score[i][j] = prev_score = prev_score + gap_score

    # backtrace to find the all indices of optimal matching
    # starting from the end to pick the first possible match we encounter
    i, j = needle_len - 1, haystack_len - 1
    # use to determine if the current match is consequtive match
    match_required = False
    indices = [0 for _ in range(needle_len)]

    while i >= 0:
        while j >= 0:
            # if the prev score is determined to be consecutive match
            # then the current position must be a match
            # e.g. haystack, needle = "auibywcabc", "abc"
            # using match_required: [7, 8, 9]
            # without match_required: [0, 8, 9]
            if (
                    match_required or running_score[i][j] == result_score[i][j]
            ) and running_score[i][j] != SCORE_MIN:
                match_required = (
                        i > 0
                        and j > 0
                        and result_score[i][j]
                        == running_score[i - 1][j - 1] + SCORE_MATCH_CONSECUTIVE
                )
                indices[i] = j
                j -= 1
                break
            else:
                j -= 1
        i -= 1

    return result_score[needle_len - 1][haystack_len - 1], indices


def _subsequence(needle: str, haystack: str) -> bool:
    if not needle:
        return True
    haystack_lowwr = haystack.lower()
    offset = 0
    for char in needle.lower():
        offset = haystack_lowwr.find(char, offset) + 1
        if offset <= 0:
            return False
    return True


def _fzy_scorer(needle: str, haystack: str) -> tuple[float, Optional[list[int]]]:
    return _score(needle, haystack) if _subsequence(needle, haystack) else (SCORE_MIN, None)


def _substr_scorer(needle: str, haystack: str) -> tuple[float, Optional[list[int]]]:
    indices = []
    offset = 0
    needle, haystack = needle.lower(), haystack.lower()

    for needle in needle.split(" "):
        if not needle:
            continue
        offset = haystack.find(needle, offset)
        if offset < 0:
            return SCORE_MIN, None
        needle_len = len(needle)
        indices.extend(range(offset, offset + needle_len))
        offset += needle_len

    if not indices:
        return 0, indices

    return (
        -(indices[-1] + 1 - indices[0]) + 2 / (indices[0] + 1) + 1 / (indices[-1] + 1),
        indices,
    )
