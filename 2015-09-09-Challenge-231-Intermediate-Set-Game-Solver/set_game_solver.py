from itertools import combinations
data = open("cards.txt").read().splitlines()

def check_valid(cards):
    for x in range(4):
        temp = []
        for card in cards:
            temp.append(card[x])

        if len(set(temp)) == 2:
            return False


for cards in combinations(data, 3):
    answerSet = ""
    if (check_valid(cards) == False):
        continue
    for card in cards:
        answerSet += card + " "
    print answerSet
