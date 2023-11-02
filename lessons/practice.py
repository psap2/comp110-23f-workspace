"""Practice for quiz 02"""

def odd_and_even(input: list[int]) -> list[int]:
    new_list: list[int] = []
    idx: int = 0
    while idx < len(input):
        if idx % 2 == 0 and input[idx] % 2 != 0:
            new_list.append(input[idx])
        idx += 1
    return new_list

def value_exists(dict_1: dict[str, int], x: int) -> bool:
    check_val: int = x
    for i in dict_1:
        if dict_1[i] == check_val:
            return True
    return False


def short_words(list1: list[str]) -> list[str]:
    character_limit: int = 5
    return_list: list[str] = []
    for words in list1:
        if len(words) >= character_limit:
            print(f" { words } is too long!")
        else:
            return_list.append(words)
    return return_list

