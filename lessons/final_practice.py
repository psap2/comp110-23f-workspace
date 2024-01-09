
def test_question(h: int) -> int:
    if h == 0:
        return h
    else:
        return 2 + test_question( h - 2)
    
    
i: int = 4
print(test_question(i))


def compareCharacters(string1: str, string2: str) -> bool:
    for i in range(len(string1)):
        if string1[i] not in string2:
            return False
    return True


def findIndices(num_list: list[int], target_num: int) -> dict[int, list[int]]:
    number_of_pairs: int = 0
    return_dict: dict[str, list[int]] = {}
    for idx1 in range(len(num_list)):
        if num_list[idx1] <= target_num:
            for idx2 in range(len(num_list)):
                if (num_list[idx1] + num_list[idx2]) is target_num:
                    number_of_pairs += 1
                    pair_string = f"{number_of_pairs} th pair: "
                    return_dict[pair_string] = [idx1, idx2]
    return return_dict

test_list: list[int] = [2, 7, 11, 15]
test_target: int = 9
print(findIndices(test_list, test_target))