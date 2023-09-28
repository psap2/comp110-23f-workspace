"""Exercise 3: Wordle."""

__author__ = "730651920"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#add appropriate function header


def contains_char(string_searched: str, string_matched: str) -> bool:
    """This function returns true if any character matches string being searched."""
    assert len(string_matched) == 1
    idx_of_searched: int = 0
    len_of_searched: int = len(string_searched)
    while idx_of_searched < len_of_searched:
        if string_searched[idx_of_searched] == string_matched:
            return True
        else:
            idx_of_searched += 1
    
    return False


def emojified(guess_string: str, secret_string: str) -> str:
    """Add appropiate Docstring."""
    assert len(guess_string) == len(secret_string)
    idx_secret: int = 0
    guess_result: str = ""
    # while the index of the secret is less than the len of the sercret 
    while idx_secret < len(secret_string):
        # run the function contains char to see if any characters are contained
        if contains_char(secret_string[idx_secret], guess_string[idx_secret]):
            guess_result += GREEN_BOX
        else:
            if contains_char(secret_string, guess_string[idx_secret]):
                guess_result += YELLOW_BOX
            else:
                guess_result += WHITE_BOX
        idx_secret += 1
    return guess_result            


def input_guess(expected_length: int) -> str:
    user_input: str = input(f"Enter a { expected_length } character word: ")
    while len(user_input) != expected_length:
        user_input = input(f"That wasn't {expected_length} chars! Try again: ")
    if len(user_input) == expected_length:
        return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # secret word as a variable
    secret_word: str = "codes"
    number_of_tries: int = 1
    game_status: bool = False
    while number_of_tries <= 6 and not game_status:
        print(f"=== Turn { number_of_tries }/6 ===")
        user_guess: str = input_guess(len(secret_word))
        emoji_result: str = emojified(user_guess, secret_word)
        print(emoji_result)
        if user_guess == secret_word: 
            game_status = True
            print(f"You won in { number_of_tries }/6 turns!")
        else:
            number_of_tries += 1
    if number_of_tries > 6:
        print("X/6 - Sorry, try again tommorow!")   


if __name__ == "__main__":
    main()  