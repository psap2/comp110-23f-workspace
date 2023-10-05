"""Testing conditonals with low card example"""

low_card: int = 3
current_card: int = 5

if current_card < low_card:
    low_card = current_card
else:
    print (str(current_card) + " is not the lowest card")
print("The lowest card is " + str(low_card))

my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)

if my_number == 10:
    print("Right!")
else:
    print("Wrong!")

print(2 + 2 / 2 ** (2 * 0))
