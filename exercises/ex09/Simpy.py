"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = 730651920


class Simpy:
    """Simpy Class."""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, list_of_float: list[float]) -> None:
        """Part 0. Simply constructor, it assigns the list of floats passed to values."""
        self.values = list_of_float

    def __str__(self) -> str:
        """Part 1. defining the string method to return a simpy object converted to a string representation."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, fill_amount: int) -> None:
        """Part 2. Fill method that mutates the values attribute of the Simpy object to fill floats with a quantity."""
        self.values = []
        for i in range(0, fill_amount):
            self.values.append(fill_value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Part 3. fill the values attribute with range of values, but in terms of floats."""
        assert step != 0.0
        current_float: float = start
        while current_float != stop:
            self.values.append(current_float)
            current_float += step
    
    def sum(self) -> float: 
        """Part 4. sum method that computes and returns the sum of all the iteams in the value attribute of the Simpy object."""
        return sum(self.values)
    
    def __add__(self, add_value: Union[float, Simpy]) -> Simpy: 
        """Part 5. Method to create a new simpy object with the float or simpy added into the simpy."""
        return_simpy: Simpy = Simpy([])
        if type(add_value) is Simpy:
            for item in range(0, len(self.values)):
                return_simpy.values.append(self.values[item] + add_value.values[item])
        else:
            for item in range(0, len(self.values)):
                return_simpy.values.append(self.values[item] + add_value)
        return return_simpy
        
    def __pow__(self, exponent_value: Union[float, Simpy]) -> Simpy:
        """Part 6. Returns a new simpy object with orginal raised to an exponenet."""
        return_simpy: Simpy = Simpy([])
        if type(exponent_value) is Simpy:
            for item in range(0, len(self.values)):
                return_simpy.values.append(self.values[item] ** exponent_value.values[item])
        else:
            for item in range(0, len(self.values)):
                return_simpy.values.append(self.values[item] ** exponent_value)
        return return_simpy
            
    def __eq__(self, equality_item: Union[float, Simpy]) -> list[bool]:
        """Part 7. Returns a mask (list of booleans) based on the quality of each item in the values attribute with some other Simpy object or a float value."""
        return_mask: list[bool] = []
        if type(equality_item) is Simpy:
            for number in range(0, len(self.values)):
                if self.values[number] == equality_item.values[number]:
                    return_mask.append(True)
                else:
                    return_mask.append(False)
        else:
            for number in range(0, len(self.values)):
                if self.values[number] == equality_item:
                    return_mask.append(True)
                else:
                    return_mask.append(False)
        return return_mask
    
    def __gt__(self, compare_value: Union[float, Simpy]) -> list[bool]:
        """Part 8. Returns a mask (list of booleans) based on the greater than relationship between each item in the values attribute with some other comparable value."""
        return_list: list[bool] = []
        if type(compare_value) is Simpy:
            for number in range(0, len(self.values)): 
                if self.values[number] > compare_value.values[number]:
                    return_list.append(True)
                else:
                    return_list.append(False)
        else:
            for number in range(0, len(self.values)):
                if self.values[number] > compare_value:
                    return_list.append(True)
                else:
                    return_list.append(False)
        return return_list
    
    def __getitem__(self, extract_item: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Part 9 & 10. Modifies the subscription operator with the Simpy objects to acess the value attribute in the class."""
        return_simpy: Simpy = Simpy([])
        if type(extract_item) is list:
            for number in range(0, len(self.values)):
                if extract_item[number] is True:
                    return_simpy.values.append(self.values[number])
        else:
            return self.values[extract_item]
        return return_simpy