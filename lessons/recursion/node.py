"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the data attribute with the first element in the linked list."""
        return_int: int
        return_int = self.data
        return return_int
    
    def tail(self) -> Node | None:
        """Returns a linked list of every element minus the head.""" 
        return self.next
    
    def last(self) -> int:
        """Returns the data of the last element in the linked list."""
        return_int: int
        if self.next is None:
            return_int = self.data
            return return_int
        else:
            return self.next.last()
        return None