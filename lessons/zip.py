"""Combining two lists into a dictionary."""

__author__ = "730651920"


def zip(key: list[str], value: list[int]) -> dict[str, int]:
    """Zip function that creates a dictionary."""
    return_dict: dict[str, int] = {}
    idx: int = 0
    if len(key) != len(value) or len(key) == 0 or len(value) == 0:
        return return_dict
    else:
        while idx < len(key):
            return_dict[key[idx]] = value[idx]
            idx += 1
        return return_dict