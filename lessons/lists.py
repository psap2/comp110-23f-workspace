"""Practice with lists"""

# intialize an empty list

groccery_list: list[str] = list()


groccery_list.append("bananas")
groccery_list.append("milk")
groccery_list.append("bread")
groccery_list[1] = "cereal"
groccery_list.pop(2)
print(groccery_list)