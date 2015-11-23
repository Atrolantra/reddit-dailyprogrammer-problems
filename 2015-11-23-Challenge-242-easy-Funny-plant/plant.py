# https://www.reddit.com/r/dailyprogrammer/comments/3twuwf/20151123_challenge_242_easy_funny_plant/

def fib_finder(aim, start):
	# Set the starting values for the fib sequence
	# based on the given starting plants.
	a,b,x = 0,start,1
	# Take two steps forward in the sequence
	# and count these steps. The plant growth
	# pattern can be exploited as a fib sequence
	# where the starting plants is a multiplier
	# and each second number is skipped.
	while a < aim:
	    a = a + b
	    b = a + b
	    x += 1
	print x

# The cases to test.
# [aim ofr plants, starting plants].
tests = [[200, 15], [50000, 1], [150000, 250]]

for x in tests:
	fib_finder(x[0], x[1])

