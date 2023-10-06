"""Exercise 4: Utils."""

__author__ = "730651920"


def all(list_of_ints: list[int], number: int) -> bool:
    """Checks if all values in list are identical."""
    if len(list_of_ints) == 0:
        return False
    list_idx: int = 0
    while list_idx < len(list_of_ints):
        if list_of_ints[list_idx] == number:
            list_idx += 1
        else:
            return False  
    return True


def max(list_of_ints: list[int]) -> int:
    """Finds the max in a list of intergers."""
    if len(list_of_ints) == 0:
        raise ValueError
    list_idx: int = 0
    Max_int: int = list_of_ints[0]
    while list_idx < len(list_of_ints):
        if list_of_ints[list_idx] > Max_int:
            Max_int = list_of_ints[list_idx]
        list_idx += 1
    return Max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if values in one list equal another in different list."""
    if list1 == list2:
        return True
    else:
        return False