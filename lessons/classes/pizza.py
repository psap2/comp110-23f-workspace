"""Defining a Class!"""


class Pizza:

    # attributes

    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gluten: bool) -> None:
        "My constructor"
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gluten
        pass

