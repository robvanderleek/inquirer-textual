import pytest

from inquirer_textual.common.pfzy import substr_scorer, _rank_task, fzy_scorer, fuzzy_match, _char_range_with, _score, \
    SCORE_MAX, _subsequence, _bonus


@pytest.mark.asyncio
async def test_rank_task() -> None:
    assert await _rank_task(substr_scorer, "abc", [{"val": "wzawbc"}], "val") == []
    assert await _rank_task(
        substr_scorer, "abc", [{"val": "wabco"}, {"val": "abcabc"}], "val"
    ) == [
               {
                   "haystack": {"val": "abcabc"},
                   "indices": [0, 1, 2],
                   "score": -0.6666666666666667,
               },
               {"haystack": {"val": "wabco"}, "indices": [1, 2, 3], "score": -1.75},
           ]

    assert await _rank_task(
        fzy_scorer,
        "abc",
        [{"val": "acbabc"}, {"val": "abcABC"}, {"val": "bwd abc"}],
        "val",
    ) == [
               {
                   "haystack": {"val": "abcABC"},
                   "indices": [0, 1, 2],
                   "score": 2.8850000000000002,
               },
               {
                   "haystack": {"val": "bwd abc"},
                   "indices": [4, 5, 6],
                   "score": 2.7800000000000002,
               },
               {
                   "haystack": {"val": "acbabc"},
                   "indices": [3, 4, 5],
                   "score": 1.9849999999999999,
               },
           ]

    assert await _rank_task(
        fzy_scorer, "ab", [{"val": "acb"}, {"val": "acbabc"}], "val"
    ) == [
               {"score": 0.98, "indices": [3, 4], "haystack": {"val": "acbabc"}},
               {"score": 0.89, "indices": [0, 2], "haystack": {"val": "acb"}},
           ]


@pytest.mark.asyncio
async def test_fuzzy_match() -> None:
    await fuzzy_match("a", ["abca"]) == [{"value": "abca", "indices": [0]}]
    await fuzzy_match(
        "a",
        [{"val": "abca"}, {"val": "aAbc"}],
        key="val",
        scorer=substr_scorer,
        batch_size=1,
    ) == [{"val": "abca", "indices": [0]}, {"val": "aAbc", "indices": [0]}]

    with pytest.raises(TypeError):
        await fuzzy_match("a", [{"val": "abc"}])


def test_char_range_with():
    result = _char_range_with("0", "9", 10, {"a": 1})
    assert result == {
        "0": 10,
        "1": 10,
        "2": 10,
        "3": 10,
        "4": 10,
        "5": 10,
        "6": 10,
        "7": 10,
        "8": 10,
        "9": 10,
        "a": 1,
    }

    result = _char_range_with("A", "D", 2, {})
    assert result == {"A": 2, "B": 2, "C": 2, "D": 2}


def test_bonus():
    assert _bonus("abc") == [0.9, 0, 0]
    assert _bonus("abc abc") == [0.9, 0, 0, 0, 0.8, 0, 0]
    assert _bonus("abc/abc") == [0.9, 0, 0, 0, 0.9, 0, 0]
    assert _bonus("abc/abC") == [0.9, 0, 0, 0, 0.9, 0, 0.7]
    assert _bonus("/abc") == [0, 0.9, 0, 0]


def test_score():
    assert _score("", "abc") == (SCORE_MAX, [])
    assert _score("abc", "abc") == (SCORE_MAX, [0, 1, 2])
    assert _score("abc", "acbabc") == (1.9849999999999999, [3, 4, 5])
    assert _score("abc", "acbABC") == (2.685, [3, 4, 5])
    assert _score("ABC", "acbABC") == (2.685, [3, 4, 5])
    assert _score("b ABC", "acb bABC") == (3.6799999999999997, [2, 3, 5, 6, 7])


def test_subsequence():
    assert _subsequence("awc", "abc") == False
    assert _subsequence("awc", "abcwc") == True
    assert _subsequence("a ui", "waui wou i") == True
    assert _subsequence("", "waui wou i") == True
    assert _subsequence('awc', 'AbCwC') == True
    assert _subsequence('AwC', 'abcwc') == True


@pytest.mark.asyncio
async def test_fuzzy_match():
    result = await fuzzy_match('i', ['Hydrogen', 'Helium', 'Lithium', 'Berylium', 'Boron', 'Carbon'],
                               scorer=substr_scorer)
    assert result[0]['value'] == 'Lithium'
    assert result[0]['indices'] == [1]
    assert result[1]['value'] == 'Helium'
    assert result[1]['indices'] == [3]
    assert result[2]['value'] == 'Berylium'
    assert result[2]['indices'] == [5]


def test_substr_scorer():
    result = substr_scorer("ab", "awsab")

    assert result[0] == -1.3
    assert result[1] == [3, 4]

    result = substr_scorer("ab", "abc")
    assert result[0] == 0.5
    assert result[1] == [0, 1]

    result = substr_scorer("ab", "iop")
    assert result[0] == -float('inf')
    assert result[1] is None

    result = substr_scorer("ab", "asdafswabc")
    assert result[0] == -1.6388888888888888
    assert result[1] == [7, 8]

    result = substr_scorer(" ", "asdf")
    assert result[0] == 0
    assert result[1] == []
