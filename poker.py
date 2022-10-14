#2,3,4,5,6,7,8,9,10,11(J), 12(D), 13(K),14(A)
import secrets
import random

global colors
colors = ["Herz", "Karo", "Pik", "Blatt"]
combination_str = ["Highcard", "Pair", "two Pairs", "Triple", "Straight", "Flush", "Poker", "Straight Flush", "Royal Flush"]

def checkHighestPair(cards):
    pairs = [0]*15
    for c in cards:
        pairs[c.symbol] += 1

    pairLvl = 0
    pairIndex = 0
    for i in range(len(pairs)-1):
        if pairLvl < pairs[i]:
            pairLvl = pairs[i]
            pairIndex = i
    if pairLvl == 4:
        return 7 #number associated with poker
    if pairLvl == 3:
        for i in range(len(pairs)):
            if pairs[i] == 2 and i != pairIndex:
                return 6 #number associated with fullhouse
        return 3 #tripple
    elif pairLvl == 2:
        for i in range(len(pairs)):
            if pairs[i] == 2 and i != pairIndex:
                return 2 #two pairs
        return 1 # number associated with pair
    else:
        return 0 #highcard

def checkStraights(cards):
    cardSymbols = []
    for c in cards:
        cardSymbols.append(c.symbol)
    cardSymbols.sort()
    flush, straight = True, True
    for i in range(len(cardSymbols)-1):
        if(cardSymbols[i]+1 != cardSymbols[i+1]):
            straight = False
        if(cards[i].color != cards[i+1].color):
            flush = False
    if(flush):
        if(straight):
            if(cardSymbols[-1] == 14):
                return 9 #royal flush
            return 8 #straight flush
        return 5 #flush
    return 4 if straight else 0 #straight

class Card:
    color: str
    symbol: int

    def __init__(self, *args):
        if(len(args)) > 0:
            self.color = args[0]
            self.symbol = args[1]
        else:
            self.color = secrets.choice(colors)
            self.symbol = random.randint(2,14)


    def __str__(self):
        return self.color + " " + str(self.symbol)

combinations = [0]*10
for i in range(1000000):
    cards = []
    for j in range(5):
        cards.append(Card())
    for k in range(len(cards)):
        #print(str(cards[k]))
        #print()
        pass

    combinations[max(checkStraights(cards), checkHighestPair(cards))] += 1

    #print(max(checkStraights(cards), checkHighestPair(cards)))

for i in range(len(combination_str)):
    print(combination_str[i] + ": " + str(combinations[i]/sum(combinations)*100) + "%")





