"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730651920"

user_inputted_word: str = input("Enter a 5 character word: ")

if len(user_inputted_word) != 5:
    print ("Error: Word must contain 5 characters")
    exit()
user_inputted_singe_character: str = input("Enter a single character: ")
if len(user_inputted_singe_character) != 1:
    print("Error: Character must be a single character")
    exit()
counter_of_inputted_character: int = 0
print("Searching for " + user_inputted_singe_character + " in " + user_inputted_word)

if user_inputted_word[0] == user_inputted_singe_character:
    print(user_inputted_singe_character + " found at index 0")
    counter_of_inputted_character += 1
if user_inputted_word[1] == user_inputted_singe_character:
    print(user_inputted_singe_character + " found at index 1")
    counter_of_inputted_character += 1
if user_inputted_word[2] == user_inputted_singe_character:
    print(user_inputted_singe_character + " found at index 2")
    counter_of_inputted_character += 1
if user_inputted_word[3] == user_inputted_singe_character:
    print(user_inputted_singe_character + " found at index 3")
    counter_of_inputted_character += 1
if user_inputted_word[4] == user_inputted_singe_character:
    print(user_inputted_singe_character + " found at index 4")
    counter_of_inputted_character += 1

if counter_of_inputted_character >= 1:
    print (str(counter_of_inputted_character) + " instances of " + user_inputted_singe_character + " found in " + user_inputted_word)
else:
    if counter_of_inputted_character == 0:
        print("No instances of " + user_inputted_singe_character + " found in " + user_inputted_singe_character)


