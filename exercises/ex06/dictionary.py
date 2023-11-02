"""Exercise 6: Dictionary Functions"""

__author__ = "730651920"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Function used to return an inverted dictionary."""
    return_dict: dict[str, str] = {}
    for key1 in d:
        for key2 in d:
            if d[key1] == d[key2] and key1 != key2:
                raise KeyError("cannot have a dictionary with the same keys")
    return_dict[d[key1]] = key1
    return return_dict


def favorite_color(d: dict[str, str]) -> str:
    """Function used to return most popular color."""
    popular_color: str = ""
    highest_count: int = 0
    count: int = 0
    for key1 in d:
        for key2 in d:
            if d[key1] == d[key2]:
                count += 1
        if highest_count < count:
            highest_count = count
            popular_color = d[key1]
    count = 0
    return popular_color


def count(list1: list[str]) -> dict[str, int]:
    """Function used to return the frequency of strings.""" 
    return_dict: dict[str, int] ={}
    count: int = 0
    for iteam1 in list1:
        for iteam2 in list1:
            if iteam1 == iteam2:
                count += 1
        return_dict[iteam1] = count
    return return_dict        


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Function used to return a list of a words alphabetized."""
    return_dict: dict[str, list[str]] = {}
    for iteam1 in list1:
        return_dict[iteam1.lower()[0]] = list()
        for iteam2 in list1:
            if iteam2.lower()[0] == iteam1.lower()[0]:
                return_dict[iteam1.lower()[0]].append(iteam2)
    return return_dict


def update_attendance(d: dict[str, list[str]], day_of_week: str, student_name: str) -> dict[str, list[str]]:
    """Function used to update the attendance."""
    updated_record = d
    if day_of_week in d:
        updated_record[day_of_week].append(student_name)
    if day_of_week not in d: 
        updated_record[day_of_week] = list()
        updated_record[day_of_week].append(student_name)