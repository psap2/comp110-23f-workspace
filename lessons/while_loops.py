"""Demonstrate while loops by finding low value in string"""

cards: str = ("5235")

card_idx: int = 0
low_card: int = int(cards[0])
#look at each number on the string
while card_idx < 4:
    #identify current card
    current_card: int = int(cards[card_idx])
    #check if current card is less than low card
    if current_card < low_card:
        low_card = current_card

    card_idx += 1
print(low_card)
print("Hello\nworld\n!!!")
age: int = 21
msg: str = f"You are {age}!"
print(msg)
