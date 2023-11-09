"""EX07: Dictionary Tests."""

__author__ = "730651920"

import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_expected_output() -> None: 
    """Function to test if invert returns an inverted dictionary."""
    test_dict: dict[str, str] = {'x': 'a', 'y': 'b', 'z': 'c'}
    expected: dict[str, str] = {'a': 'x', 'b': 'y', 'c': 'z'}
    assert invert(test_dict) == expected


def test_invert_int() -> None:
    """Function to test if invert returns a inverted dictionary with integers."""    
    test_dict: dict[int, int] = {1: 10, 2: 20, 3: 30}
    expected: dict[int, int] = {10: 1, 20: 2, 30: 3}
    assert invert(test_dict) == expected


def test_invert_with_same_keys() -> None:
    """Function to test if invert raises key error when given a dictionary with same values which causes error in the invertest dictionary."""
    with pytest.raises(KeyError):
        test_dict = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(test_dict)


def test_favorite_color_expected_outcome() -> None: 
    """Function to test if favorite color returns the most popular color."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    expected: str = "blue"
    assert favorite_color(test_dict) == expected


def test_favorite_color_same_favorite_color() -> None: 
    """Function to test if favorite color returns the first popular color when given a tie for the most frequent colors."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Prasun": "yellow"}
    expected: str = "yellow"
    assert favorite_color(test_dict) == expected


def test_favorite_color_one_color() -> None:
    """Function to test if favorite color returns only 1 color given there is only 1 color in dictionary."""
    test_dict: dict[str, str] = {"Marc": "yellow"}
    expected: str = "yellow"
    assert favorite_color(test_dict) == expected 


def test_count_expected_outcome() -> None:
    """Function to test if count returns the correct dictionary with the correct count."""
    test_list: list[str] = ["prasun", "kishan", "dan", "kishan", "dan", "kishan", "kunal", "ayush", "ayush"]
    expected: dict[str, int] = {"prasun": 1, "kishan": 3, "dan": 2, "kunal": 1, "ayush": 2}
    assert count(test_list) == expected


def test_count_given_one_string() -> None:
    """Function to test if count returns correct dictionary given there is only 1 name string in the list."""
    test_list: list[str] = ["prasun"]
    expected: dict[str, int] = {"prasun": 1}
    assert count(test_list) == expected


def test_count_given_empty_list() -> None: 
    """Function to test if count returns a correct dictionary given there is nothing in list."""
    test_list: list[str] = []
    expected: dict[str, int] = {}
    assert count(test_list) == expected


def test_alphabetizer_expected_outcome() -> None: 
    """Function to test if alphabetizer actually returns a correct dictionary that satisfies its utility."""
    test_list: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    expected: dict[str, list[str]] = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert alphabetizer(test_list) == expected


def test_alphabetizer_with_capitals() -> None: 
    """Function to test if alphabetizer actually returns a correct dictionary that satisfies its utility given capitals."""
    test_list: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    expected: dict[str, list[str]] = {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}
    assert alphabetizer(test_list) == expected


def test_alphabetizer_with_empty_list() -> None:
    """Function to test if alphabetizer returns an empty dictionary given a empty list."""
    test_list: list[str] = []
    expcted: dict[str, list[str]] = {}
    assert alphabetizer(test_list) == expcted


def test_update_attendence_expected_outcome() -> None:
    """Function to test if update attendence returns a correct list with correct attendence."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    expected: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}
    assert update_attendance(attendance_log, "Tuesday", "Vrinda") == expected


def test_update_attendence_two_updates_outcome() -> None:
    """Function to test if update attendence returns a correct list given 3 updates attendence."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    expected: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda", "Prasun"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    assert update_attendance(attendance_log, "Tuesday", "Prasun") == expected


def test_update_attendence_three_updates_outcome() -> None:
    """Function to test if update attendence returns a correct list given 2 updates attendence."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    expected: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb", "Ayush"], "Tuesday": ["Alyssa", "Vrinda", "Prasun"]}
    update_attendance(attendance_log, "Monday" , "Ayush")
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    assert update_attendance(attendance_log, "Tuesday", "Prasun") == expected