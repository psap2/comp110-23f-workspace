"""File to define Bear class."""


class Bear:
    """Bear class that creates the bear object with an age and hunger score and has different methods."""
    age: int
    hunger_score: int
    
    def __init__(self, inp_age: int = 0, inp_hunger_score: int = 0):
        """Intilizes the object with an age and hunger score."""
        self.age = inp_age
        self.hunger_score = inp_hunger_score
        return None
    
    def one_day(self):
        """Method to update the age and hunger score of a bear after one simulated day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Method to update the hunger score of a bear after an instance of eating."""
        self.hunger_score += num_fish