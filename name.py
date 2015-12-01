import os
import re
# 2015-11-25-Challenge-242-Intermediate-VHS-recording-problem
# 243 [Easy] Abundant and Deficient Numbers

def edited(path):
	num = re.search('nge-(.*)-[I|E|H]', path).group(1)
	difficulty = re.search('-(Inter[^-]*|Hard|Easy)-', path).group(1)
	namestring = difficulty + '-(.*)'
	name = re.search(namestring, path).group(1).replace('-', ' ')
	return num + ' ' + '[' + difficulty + ']' + ' ' + name





for x in os.walk("C:\Users\Eric\Documents\GitHub\/reddit-dailyprogrammer-problems"):
	for y in x:
		if "2015" in y:
			os.rename(y, edited(y))