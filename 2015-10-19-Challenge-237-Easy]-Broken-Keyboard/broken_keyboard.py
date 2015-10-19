# https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/
dictWordList = open('enable1.txt').read().splitlines()
inputs = ["edcf", "bnik", "poil", "vybu"]

def check(keyString):
	longest = max(len(entry) for entry in dictWordList if (set(entry).issubset(set(keyString))))
	result = list(entry for entry in dictWordList if (len(entry) == longest and set(entry).issubset(set(keyString))))
	return result

for word in inputs:
    print check(word)
