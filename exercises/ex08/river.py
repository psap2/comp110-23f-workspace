"""File to define River class."""

__author__ = "730651920"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River class that creates the river object with an enviorment of fishes and bears and has methods to stimulate a real ecosystem."""
    day: int
    bears: list[Bear] = []
    fish: list[Fish] = []
   
    def __init__(self, num_fish: int, num_bears: int):
        """Intializes River object with a new River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the age of the bears and fish to make sure they are old enough to be living. If they are to old they are removed from the population."""
        updated_bear_list: list[Bear] = []
        updated_fish_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                updated_fish_list.append(fish)
        self.fish = updated_fish_list
        for bears in self.bears:
            if bears.age <= 5:
                updated_bear_list.append(bears)
        self.bears = updated_bear_list
        return None

    def bears_eating(self):
        """Stimulates bear eating, meaning for every bear there must be 5 fish and of which 3 are consumed."""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                Bear().eat(3)

        return None
    
    def check_hunger(self):
        """Checks the hunger of the bear by checking if starvation occured in which case it did, the bear is removed from the population."""
        updated_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                updated_bear_list.append(bear)
        self.bears = updated_bear_list
        return None
        
    def repopulate_fish(self):
        """Stimulates reproduction of a fish, meaning for every 2 fish, four is birthed and appended into the population."""
        number_of_fishs: int = len(self.fish)
        number_of_reproduced_fishs: int = (number_of_fishs // 2) * 4
        for number in range(0, number_of_reproduced_fishs):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Stimulates reproduction of a bear, meaning for every 2 bears, one is birthed and appended into the population."""
        number_of_bears: int = len(self.bears)
        number_of_reproduced_bears: int = (number_of_bears // 2)
        for number in range(0, number_of_reproduced_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """View river method to output the day number, fish population, and bear population."""
        output: str = (f"~~~ Day {self.day}: ~~~\nFish Population: {len(self.fish)}\nBear Population: {len(self.bears)}")
        print(output)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            Bear().one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            Fish().one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Stimulates one river week by calling the one river day method 7 times."""
        for loop_number in range(0, 7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Method used to remove a certain number of fish, used during bears eating method."""
        for number in range(0, amount):
            self.fish.pop(number)