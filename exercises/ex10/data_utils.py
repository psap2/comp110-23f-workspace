"""Dictionary related utility functions."""

__author__ = 730651920

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    # this thing just opens the file and reads it
    file_handle = open(filename, "r", encoding="utf8")
    # now use DictReader object to read the file 
    csv_reader = DictReader(file_handle)
    # this csv reader is something that can be looped throug with rows 
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        # save every value under key header
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table repreesented as a list of rows into one represented as a dictionary of column."""
    result: dict[str, list[str]] = {}
    for row in table:
        for column_name in row:
            result[column_name] = column_values(table, column_name)
    return result


def head(table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if row_number >= len(table):
        row_number = len(table)
    for column_name in table:
        assigning_list: list[str] = []
        for idx in range(row_number):
            values_in_column: list[str] = table[column_name]
            assigning_list.append(values_in_column[idx])
        result[column_name] = assigning_list
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only specified columns."""
    result: dict[str, list[str]] = {}
    for column_names in columns:
        result[column_names] = table[column_names]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table by concatting two column-based tables."""
    result: dict[str, list[str]] = {}
    for columns1 in table1:
        result[columns1] = table1[columns1]
    for columns2 in table2:
        if columns2 in result:
            result[columns2].extend(table2[columns2])
        else: 
            result[columns2] = table2[columns2]
    return result


def count(strings_to_count: list[str]) -> dict[str, int]:
    """Gives a list of strings this function produces a dictionary of keys of the string and value as the count of that string."""
    result: dict[str, int] = {}
    for string in strings_to_count:
        if string in result:
            result[string] += 1
        else:
            result[string] = 1
    return result