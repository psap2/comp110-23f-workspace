"""Exercise 3: Wordle."""

__author__ = "730651920"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(string_searched: str, string_matched: str) -> bool:
    """This function returns true if any character matches string being searched."""
    assert len(string_matched) == 1
    idx_of_searched: int = 0
    len_of_searched: int = len(string_searched)
    # Checks if any character is matched with the string being searched
    while idx_of_searched < len_of_searched:
        if string_searched[idx_of_searched] == string_matched:
            return True
        else:
            idx_of_searched += 1       
    return False


def emojified(guess_string: str, secret_string: str) -> str:
    """Function inserts emoji's for characters matched for string."""
    assert len(guess_string) == len(secret_string)
    idx_secret: int = 0
    # what the function will return based on the guess string and secret string
    guess_result: str = ""
    # while the index of the secret is less than the len of the sercret 
    while idx_secret < len(secret_string):
        # run the function contains char to see if any characters are contained
        if contains_char(secret_string[idx_secret], guess_string[idx_secret]):
            guess_result += GREEN_BOX
        else:  # checking if any characters are included in the secret string but just not in the right spot
            if contains_char(secret_string, guess_string[idx_secret]):
                guess_result += YELLOW_BOX
            else:
                guess_result += WHITE_BOX
        idx_secret += 1
    return guess_result            


def input_guess(expected_length: int) -> str:
    """Function to guide user to input the correct word number guess."""
    user_input: str = input(f"Enter a { expected_length } character word: ")
    # lets the user to try again if the word length of the guess is not matched
    while len(user_input) != expected_length:
        user_input = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # secret word as a variable
    secret_word: str = "codes"
    # counter variable for the number of tries
    number_of_tries: int = 1
    # boolean to check if the user has guessed the correct word
    game_status: bool = False
    # loops through the game while the user has less than 6 tries and has not yet won the game
    while number_of_tries <= 6 and not game_status:
        print(f"=== Turn { number_of_tries }/6 ===")
        # asigns the user's guess as the correct lenght word inputted by the input_guess function
        user_guess: str = input_guess(len(secret_word))
        # assigns the result of the emojis from the return of the emojified function that passes the user's guess and the secret word that can be changed as the arguments
        emoji_result: str = emojified(user_guess, secret_word)
        print(emoji_result)
        if user_guess == secret_word: 
            game_status = True
            print(f"You won in { number_of_tries }/6 turns!")
        else:
            # adds the number of tries if the user has not guessed the word correctly
            number_of_tries += 1
    if number_of_tries > 6:
        print("X/6 - Sorry, try again tommorow!")   


if __name__ == "__main__":
    main()  