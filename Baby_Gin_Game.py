"""
input 6 cards
if 3 numbers are serial, run
if 3 numbers are same, triplete.
If 6 cards are be composed of runs and tripletes, Baby-gin

Make Baby-gin using Permutation(nPr)
"""
import random
numlist = [1,2,3,4,5,6,7,8,9]
cards = [random.choice(numlist) for i in range(6)]
print(cards)
def Babygin(cards):
    result = ""
    cards.sort()
    for i in range(4):
        if cards[i] == cards[i+1] and cards[i] == cards[i+2]:
            result += "triplete "
        elif cards[i] == cards[i+1]-1 and cards[i] == cards[i+2]-2:
            result += "run "
    if len(result) == 0:
        result = "nothing"
    return result

print(Babygin(cards))
