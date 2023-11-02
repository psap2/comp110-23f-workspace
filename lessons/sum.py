"""Summing the elements of a list using different loops."""

__author__ = "730651920"

vals: list[float] = [1.1, 0.9, 1.0]


def w_sum(list_of_floats: list[float]) -> float:
    """Returns sum of list of floats using while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(list_of_floats):
        sum += list_of_floats[idx]
        idx += 1
    return sum


print(w_sum(vals))


def f_sum(list_of_floats: list[float]) -> float:
    """Returns sum of list of floats using for...in... loops."""
    sum: float = 0.0
    for float in list_of_floats:
        sum += float
    return sum


print(f_sum(vals))


def f_range_sum(list_of_floats: list[float]) -> float:
    """Returns sum of list of floats using range in for-in loops."""
    sum: float = 0.0
    for idx in range(0, len(list_of_floats)):
        sum += list_of_floats[idx]
    return sum


print(f_range_sum(vals))