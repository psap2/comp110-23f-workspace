"""One shot wordle """


__author__ = "730651920"
#Given color variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#Variables for secret word and guess word and their respective lenghts
secret_word: str = "python"
len_secret_word: int = len(secret_word)
guess_word: str = input(f"What is your { len_secret_word }-letter guess? ")
guess_word_len: int = len(guess_word)
#Index variable that will be looped through to check for matches
indx_of_word: int = 0
resulting_emoji: str = ""
#Loop to ensure the user-inputted word is the same length as secret word
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not { len_secret_word } letters! Try again: ")
#Large loop checking each character for matches, no matches, and placements    
while indx_of_word < len_secret_word:
    if guess_word[indx_of_word] == secret_word[indx_of_word]:
        resulting_emoji += GREEN_BOX
    else:
        #intilaizes variable that will be used to loop through and look for character in wrong places
        character_check_in_other_places: bool = False
        alternate_indices_of_secret: int = 0
        #loop that looks for character in wrong places
        while not character_check_in_other_places and alternate_indices_of_secret < len_secret_word:
            if secret_word[alternate_indices_of_secret] == guess_word[indx_of_word] :
                #if at the index of the guess word matches any character from secret word it adds yellow box & terminates the loop
                character_check_in_other_places = True
                resulting_emoji += YELLOW_BOX
            #if current index of secret word isn't the same as the outerloops's index of the guess' character than move to the next index of secret word
            else:
                alternate_indices_of_secret += 1
        #if there is no match at all and at the end of the while loop then just add a white box for the guess' character       
        if not character_check_in_other_places:
            resulting_emoji += WHITE_BOX
    #adds to the guess' index to prevent the outer while loop from running forever
    indx_of_word += 1
print(resulting_emoji)
#adds a final message for user
if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")