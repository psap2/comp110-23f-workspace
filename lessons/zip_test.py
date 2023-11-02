"""Test my zip function."""

__author__ = "730651920"
from lessons.zip import zip 


def test_blank_list() -> None:
    """Function testing output when given blank arguments."""
    assert zip([],[]) == {}


def test_equal_lists() -> None:
    """Function testing if lists are equal lengths."""
    key = ["a", "b", "c"]
    value = [1, 2, 3]
    expected = {"a": 1, "b": 2, "c": 3}
    assert zip(key, value) == expected


def test_unequal_lists() -> None:
    """Function tetsing if lists are unequal lengths."""
    key = ["a", "b", "c", "d"]
    value = [1, 2, 3]
    expected = {}
    assert zip(key, value) == expected

