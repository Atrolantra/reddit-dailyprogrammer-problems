# https://www.reddit.com/r/dailyprogrammer/comments/3n55f3/20150930_challenge_234_intermediate_red_squiggles/
dictWordList = open('enable1.txt').read().splitlines()
checkWordList = open ('words.txt').read().splitlines()

import string

def check(word):
    for i in range(len(word)):
        wordSlice = word[:i + 1]
        if any(entry.startswith(wordSlice) for entry in dictWordList):
            pass
        else:
        	return wordSlice + '<' + word[i + 1:]


for word in checkWordList:
    print check(word)