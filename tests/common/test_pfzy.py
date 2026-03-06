from inquirer_textual.common.Candidate import Candidate
from inquirer_textual.common.pfzy import (_substr_scorer, _rank_task, _fzy_scorer, fuzzy_match, _char_range_with,
                                          _score, \
    SCORE_MAX, _subsequence, _bonus, substr_match)


def test_rank_task() -> None:
    result = _rank_task(_substr_scorer, "abc", ["wzawbc"])
    assert result == []

    assert _rank_task(_substr_scorer, "abc", ["wabco", "abcabc"]) == [
        {
            "haystack": "abcabc",
            "indices": [0, 1, 2],
            "score": -0.6666666666666667,
        },
        {"haystack": "wabco", "indices": [1, 2, 3], "score": -1.75},
    ]

    assert _rank_task(
        _fzy_scorer,
        "abc",
        ["acbabc", "abcABC", "bwd abc"]
    ) == [
               {
                   "haystack": "abcABC",
                   "indices": [0, 1, 2],
                   "score": 2.8850000000000002,
               },
               {
                   "haystack": "bwd abc",
                   "indices": [4, 5, 6],
                   "score": 2.7800000000000002,
               },
               {
                   "haystack": "acbabc",
                   "indices": [3, 4, 5],
                   "score": 1.9849999999999999,
               },
           ]

    assert _rank_task(
        _fzy_scorer, "ab", ["acb", "acbabc"]) == [
               {"score": 0.98, "indices": [3, 4], "haystack": "acbabc"},
               {"score": 0.89, "indices": [0, 2], "haystack": "acb"},
           ]


def test_char_range_with():
    result = _char_range_with("a", "d", 1, {})
    assert result == {'a': 1, 'b': 1, 'c': 1, 'd': 1}

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
    assert _bonus("asdf") == [0.9, 0, 0, 0]
    assert _bonus("asdf asdf") == [0.9, 0, 0, 0, 0, 0.8, 0, 0, 0]
    assert _bonus("asdf aSdf") == [0.9, 0, 0, 0, 0, 0.8, 0.7, 0, 0]
    assert _bonus("asdf/aSdf") == [0.9, 0, 0, 0, 0, 0.9, 0.7, 0, 0]
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


def test_fuzzy_match():
    result = fuzzy_match("a", ["abca"])
    assert result == [{"value": "abca", "indices": [0]}]

    result = fuzzy_match("a", ["abca", "aAbc"])
    assert result == [{"value": "abca", "indices": [0]}, {"value": "aAbc", "indices": [0]}]

    result = fuzzy_match('i', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon'])
    assert result[0]['value'] == 'Helium'
    assert result[0]['indices'] == [3]
    assert result[1]['value'] == 'Lithium'
    assert result[1]['indices'] == [4]
    assert result[2]['value'] == 'Beryllium'
    assert result[2]['indices'] == [6]


def test_substr_match():
    result = substr_match("a", ["abca"])
    assert result == [Candidate("abca", [0])]

    result = substr_match("a", ["abca", "aAbc"])
    assert result == [Candidate("abca", [0]), Candidate("aAbc", [0])]

    result = substr_match('i', ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon'])
    assert result[0].choice == 'Lithium'
    assert result[0].match_indices == [1]
    assert result[1].choice == 'Helium'
    assert result[1].match_indices == [3]
    assert result[2].choice == 'Beryllium'
    assert result[2].match_indices == [6]


def test_substr_scorer():
    result = _substr_scorer("ab", "awsab")

    assert result[0] == -1.3
    assert result[1] == [3, 4]

    result = _substr_scorer("ab", "abc")
    assert result[0] == 0.5
    assert result[1] == [0, 1]

    result = _substr_scorer("ab", "iop")
    assert result[0] == -float('inf')
    assert result[1] is None

    result = _substr_scorer("ab", "asdafswabc")
    assert result[0] == -1.6388888888888888
    assert result[1] == [7, 8]

    result = _substr_scorer(" ", "asdf")
    assert result[0] == -float('inf')
    assert result[1] is None
