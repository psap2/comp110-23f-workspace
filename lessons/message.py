"""Class to storea message (operator overload, union types, default parameters)."""

__author__ = "730651920"

class Message:

    to: str | int
    content: str
    important: bool


    def __init__(self, recipient: str | int, message: str = "", important_message: bool = False) -> None:
        """Constructor for a message."""
        self.to = recipient
        self.content = message
        self.important = important_message


    def __str__(self) -> str:
        """Output message."""
        output: str = f"Message to { self.to }: \n"     
        output += f"Important? { self.important } \n"
        output += f"{ self.content }"
        return output


    def __mul__(self, factor: int):
        """Multiplication operator overload."""   
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val

msg_to_kishan: Message = Message("Kishan", "How are you this smart???", True)
print(msg_to_kishan)
msg_to_kishan * 3 
print(msg_to_kishan)