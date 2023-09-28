"""hiii"""

def input_guess(expected_length: int) -> str:
    """Add appropriate docstring."""
    user_input: str = input(f"Enter a { expected_length } character word: ")
    while len(user_input) != expected_length:
        user_input = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_input
    
print(input_guess(5))