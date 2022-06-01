import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


def test_one_each():
    left = {
        "key": "Hello",
    }
    right = {
        "key": "world",
    }
    expected = [
        ["key", "Hello", "world"],
    ]
    actual = left_join(left, right)
    assert sorted(actual) == sorted(expected)


def test_no_common():
    left = {
        "left": "Hello",
    }
    right = {
        "right": "world",
    }
    expected = [
        ["left", "Hello", None],
    ]
    actual = left_join(left, right)
    assert sorted(actual) == sorted(expected)


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }
    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["guide", "usher", "follow"],
    ]
    actual = left_join(synonyms, antonyms)
    assert sorted(actual) == sorted(expected)
