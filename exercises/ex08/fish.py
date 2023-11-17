"""File to define Fish class."""


class Fish:
    """Fish class that creates the fish object with an age and has different methods."""
    age: int

    def __init__(self, inp_age: int = 0):
        """Intilizes the object with an age."""
        self.age = inp_age 
        return None

    def one_day(self):
        """Method to update the age and fish after one simulated day."""
        self.age += 1
        return None