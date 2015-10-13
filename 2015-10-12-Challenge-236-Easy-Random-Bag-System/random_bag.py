# https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/
from random import shuffle
pieces = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
LENGTH = 50

# Function to make the output of pieces as if pulled from bags of 7.
def generateString(length):
	output = ""
	while (len(output) <= length):
		shuffle(pieces)
		output += "".join(pieces)
	return output[:length]

# Verify that a given string is valid according to the pattern and rules
# that pieces are selected and given in.
def verifyString(inputString):
	for x in range(len(inputString) / 7 + 1):
		testString = inputString[x * 7: (x + 1) * 7]
		if sorted(list(set(testString))) == sorted(testString):
			continue
		else: 
			return "Not valid"
	return "Valid"

tetroString = generateString(LENGTH)
print tetroString
print verifyString(tetroString)