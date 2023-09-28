"""Learning functions"""

def find_max(x1: int, x2: int) -> int:
    """ Returns the maximum value out two numbers"""
    if x1 >= x2:
        return x1
    else: #if x1 < x2
        return x2
    
def mimic(word: str) -> str:
    return word

def mimic_idx(word1: str, idx: int) -> str:
    if idx >= len(word1):
        return("Index too high")
    else:
        return(word1[idx])
    
print(mimic_idx("Prasun", 2))    





print(mimic("hello"))

word: str = "Prasun"
response: str = mimic(word)
print(response)



max_number: int = find_max(5,89)
print(max_number)