"""Practicing Counters"""

# Intialize the string I want to count the odds of
num_string: str = "123"
# Intialize my counter for the number of odds
num_of_odds: int = 0 

if int(num_string[0]) % 2 == 1  :
    num_of_odds = num_of_odds + 1
if int(num_string[1]) % 2 == 1 :
    num_of_odds = num_of_odds + 1
if int(num_string[2]) % 2 == 1 :
    num_of_odds = num_of_odds + 1
 
print (num_of_odds)

