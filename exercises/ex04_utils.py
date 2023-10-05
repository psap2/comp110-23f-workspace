"""Exercise 4: Utils."""

__author__ = "730651920"


def all (list_of_ints: list, number: int ) -> bool:
    list_idx: int = 1
    if list_of_ints[list_idx] == number:
        while list_idx < len(list_of_ints):
          if list_of_ints[list_idx-1] == list_of_ints[list_idx]:
            list_idx += 1
            return True
          else:
            list_idx = len(list_of_ints) 
            return False   
    else:
       return False
        
def max (list_of_ints: list) -> int:
    if len(list_of_ints) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 1
    Max_int: int = list_of_ints[0]
    while list_idx < len(list_of_ints):
        if list_of_ints[list_idx-1] <= list_of_ints[list_idx]:
            Max_int = list_of_ints[list_idx]
        list_idx += 1
    return Max_int
   
def lol_equal(list1: list, list2: list) -> bool:
   if list1 == list2:
      return True
   else:
      return False
   
print(lol_equal([1, 0, 1], [1, 0, 1, 0]))




    
   
    




    


