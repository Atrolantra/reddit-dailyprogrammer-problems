# https://www.reddit.com/r/dailyprogrammer/comments/3opin7/20151014_challenge_236_intermediate_fibonacciish/
from timeit import default_timer as timer

# Generator to make the Fibonacci sequence so that
# it only returns the sequence up to up to
# number x or one number bigger.
def fib_finder(x):
	a,b = 0,1
	yield a
	yield b
	while b < x:
	    a, b = b, a + b
	    yield b

def fib_maker(noFame):
	if noFame == 0:
		return ['0']
	if noFame == 1:
		return ['1']
	# Make a list with our sequence
	fibSequence = [x for x in fib_finder(noFame)]
	# Search the sequence from the back as we are 
	# looking for the biggest factor in noFame.
	for y in reversed(fibSequence):
		if noFame % y == 0:
			divvy = noFame / y
			index = fibSequence.index(y)
			break
	# Chop up the list to the biggest factor number's index
	outSequence = fibSequence[:index + 1]
	# The list we're after will be that multiplied
	# by that multiple due to a quirk in how the 
	# Fibonacci Series works.
	return [str(x * divvy) for x in outSequence]

challenge_inputs = [0, 21, 84, 578, 123456789, 38695577906193299]

file = open("output and times.txt",'w')

# For every challenge input print the answer and time taken.
for x in challenge_inputs:
	start = timer()
	out = fib_maker(x)
	end = timer()

	file.write(str(out) + "\n")
	file.write("My program took " + str(end - start) + " to run \n")
	file.write("\n")