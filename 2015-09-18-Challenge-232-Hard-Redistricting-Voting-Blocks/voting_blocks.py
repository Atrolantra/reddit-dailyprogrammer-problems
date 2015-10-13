# https://www.reddit.com/r/dailyprogrammer/comments/3lf3i2/20150918_challenge_232_hard_redistricting_voting/
import numpy as np
import math
from decimal import *
import math

getcontext().prec = 30

linesToDraw = input("How many lines to draw: ")
zones = linesToDraw + 1
cols_count = 20
rows_count = 20
output_file_name = "map.txt"
input_file_name = "raw_data.txt"

results = []

# Class to help define a subzone of a bigger zone. 
# Helpful to keep track of where zones start and end
# throughout the program.
class subZone:
	'Class for subzones of the big area'
	def __init__(self, zone, startRelativeWhole, finRelativeWhole):
		self.zone = zone
		self.startRelativeWhole = startRelativeWhole
		self.finRelativeWhole = finRelativeWhole

# Function to decide if a vertical or horizontal line needs to be drawn
# and draws it.
def drawLine(inputZone1, inputZone2):
	vert = None
	if (inputZone1.startRelativeWhole[0] == inputZone2.finRelativeWhole[0]):
		vert = True
		first = inputZone2
		second = inputZone1
	elif (inputZone1.finRelativeWhole[0] == inputZone2.startRelativeWhole[0]):
		vert = True
		first = inputZone1
		second = inputZone2

	elif (inputZone1.startRelativeWhole[1] == inputZone2.finRelativeWhole[1]):
		vert = False
		first = inputZone2
		second = inputZone1

	elif (inputZone1.finRelativeWhole[1] == inputZone2.startRelativeWhole[1]):
		vert = False
		first = inputZone1
		second = inputZone2

	if vert:
		start = second.startRelativeWhole
		fin = first.finRelativeWhole
		for x in range(start[1]*2, fin[1]*2-1):
			districtMap[x][start[0]*2-1] = '|'

	else:
		start = second.startRelativeWhole
		fin = first.finRelativeWhole
		for x in range(start[0]*2, fin[0]*2-1):
			districtMap[start[1]*2-1][x] = '-'
# The main function, takes the original whole input area
# and the number of zones required and chops it up.
def ShortestSplitLine(inputZone, desiredZones):
	global results

	if desiredZones == 1:
		file.write(str(inputZone.zone.sum()) + "\n")

		results.append(inputZone.zone.sum())

		return inputZone
	a = math.floor(desiredZones / 2.0)
	b = math.ceil(desiredZones / 2.0)

	ratioOutput, sa, sb = zoneCalculator(inputZone, a, b)

	ShortestSplitLine(sa, a)
	ShortestSplitLine(sb, b)

# Returns a subzone of a given input zone after specifying two corners.
def zoneMaker(inputZone, topLeftCorner, bottomRightCorner):
	return subZone((inputZone.zone[topLeftCorner[1]:bottomRightCorner[1], topLeftCorner[0]:bottomRightCorner[0]]), \
	(inputZone.startRelativeWhole[0] + topLeftCorner[0], inputZone.startRelativeWhole[1] + topLeftCorner[1]), \
	(inputZone.startRelativeWhole[0] + topLeftCorner[0] + (bottomRightCorner[0] - topLeftCorner[0]), \
	inputZone.startRelativeWhole[1] + topLeftCorner[1] + (bottomRightCorner[1] - topLeftCorner[1])))
	
# Determines if challenging data gives a better ration than the current best data.
def ratioCalculator(bestRatio, desiredRatio, ratio, bestRatioA, bestRatioB, aZone, bZone):
	if bestRatio == None:
		return (ratio, aZone, bZone)
	else:
		if (abs(ratio - desiredRatio) < abs(bestRatio - desiredRatio)):
			return (ratio, aZone, bZone)
		else:
			return (bestRatio, bestRatioA, bestRatioB)

# Calculate with the normal ratio.
def normRatio(bestRatio, desiredRatio, bestRatioA, bestRatioB, aZone, bZone):

	try:
		ratio = Decimal(aZone.zone.sum()) / (bZone.zone.sum() + aZone.zone.sum())
		return ratioCalculator(bestRatio, desiredRatio, ratio, bestRatioA, bestRatioB, aZone, bZone)
	except ZeroDivisionError:
		pass

# And also with an inverted ratio. 
# Ratio will be the same effectively but there's a better 
# chance for a more even/accurate output in the zoning.
def inverseRatio(bestRatioInverse, desiredRatioInverse, bestRatioAInverse, \
				 bestRatioBInverse, aZone, bZone):
	try:
		ratio = Decimal(aZone.zone.sum()) / (bZone.zone.sum() + aZone.zone.sum())
		return ratioCalculator(bestRatioInverse, desiredRatioInverse, ratio, \
							   bestRatioAInverse, bestRatioBInverse, aZone, bZone)
	except ZeroDivisionError:
		pass

def giveRatio(first, second):
	return Decimal(first) / Decimal(first + second)

def zoneCalculator(inputZone, ratioA, ratioB):
	
	bestRatio = None
	bestRatioInverse = None

	bestRatioA = None
	bestRatioAInverse = None

	bestRatioB = None
	bestRatioBInverse = None

	desiredRatio = giveRatio(ratioA, ratioB)
	desiredRatioInverse = giveRatio(ratioB, ratioA)

	zoneHeight, zoneWidth = inputZone.zone.shape

	# Calculations for potential horizontal line.
	for x in range(1, zoneWidth):
		aZone = zoneMaker(inputZone, (0, 0), (0 + x, zoneHeight))
		bZone = zoneMaker(inputZone, (zoneWidth - (zoneWidth - x), 0), (zoneWidth, zoneHeight))

		bestRatio, bestRatioA, bestRatioB = \
			normRatio(bestRatio, desiredRatio, bestRatioA, bestRatioB, aZone, bZone)
		bestRatioInverse, bestRatioAInverse, bestRatioBInverse = \
			inverseRatio(bestRatioInverse, desiredRatioInverse, bestRatioAInverse, bestRatioBInverse, aZone, bZone)

	# Calculations for potential vertical line.
	for y in range(1, zoneHeight):
		aZone = zoneMaker(inputZone, (0, 0), (zoneWidth, 0 + y))
		bZone = zoneMaker(inputZone, (0, zoneHeight - (zoneHeight - y)), (zoneWidth, zoneHeight))


		bestRatio, bestRatioA, bestRatioB = \
			normRatio(bestRatio, desiredRatio, bestRatioA, bestRatioB, aZone, bZone)
		bestRatioInverse, bestRatioAInverse, bestRatioBInverse = \
			inverseRatio(bestRatioInverse, desiredRatioInverse, bestRatioAInverse, bestRatioBInverse, aZone, bZone)

	# After running all possible line placement situations, 
	# return the two hemistates that give the best ratio.
	# Also call drawLine so that dividing boundaries
	# are drawn as the program runs.
	try:
		if (abs(bestRatio - desiredRatio) < abs(bestRatioInverse - desiredRatioInverse)):
			drawLine(bestRatioA, bestRatioB)
			return (bestRatio, bestRatioA, bestRatioB)
		else:
			drawLine(bestRatioAInverse, bestRatioBInverse)
			return (bestRatioInverse, bestRatioBInverse, bestRatioAInverse)
	except TypeError:
		if bestRatio == None:
			drawLine(bestRatioAInverse, bestRatioBInverse)
			return (bestRatioInverse, bestRatioBInverse, bestRatioAInverse)
		else:
			drawLine(bestRatioA, bestRatioB)
			return (bestRatio, bestRatioA, bestRatioB)

# The output file.
file = open(output_file_name,'w')

# The raw data file.
data = open(input_file_name).read().splitlines()
districtData = []
districtMapData = []
temp = []

empty = []
for x in range(cols_count * 2 - 1):
	empty.append(' ') 

for x in data:
	for y in x.split(' '):
		districtData.append(int(y))

		temp.append(y)
	temp = list(' '.join(temp))
	districtMapData.append(temp)
	temp = []


for _ in range(1, rows_count * 2 - 1, 2):
	districtMapData.insert(_, empty)

wholeDistrict = np.array(districtData, ndmin=2).reshape((cols_count, rows_count))
districtMap = np.array(districtMapData, ndmin=2).reshape((cols_count * 2 - 1, rows_count * 2 - 1))

# Define the starting input as the whole zone of raw data and begin the program.
startingInput = subZone(wholeDistrict, (0,0), (20,20))
ShortestSplitLine(startingInput, zones)

aim = wholeDistrict.sum() / float(zones)
error = 0

for population in results:
	error += abs(population - aim) 

file.write("Lines drawn: " + str(linesToDraw) + "\n")
file.write("Zones: " + str(linesToDraw + 1) + "\n")
file.write("Ideal people per zone is " + str(aim) + "\n")
file.write("Error (sum of the absolute value of the deviation from the ideal population in each zone) is:  " + str(error) + "\n")
file.write("\n")

for _ in districtMap:
	for a in _:
		file.write(str(a))
	file.write('\n')

file.close()
