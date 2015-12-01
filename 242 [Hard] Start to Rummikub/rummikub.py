from itertools import combinations
import random

tiles = "P7 R5 Y2 Y13 R9 B5 P3 P7 R3 Y8 P2 B7 B6 B12"

def makeColorSets(color_sets):
	run_combos = []

	# Function so that we can sort tiles by their number
	# taking into account those with double digits.
	def MyFn(s):
		return int(s[1:])

	# Check each color list for consecutive sequences.
	for x in color_sets:
		for y in range(3, len(x) + 1):
			for combo in combinations(x, y):
				# If it's a valid sequence, add it to the major setlist.
				sorted_combo = sorted(combo, key = MyFn)
				sorted_combo_nums = [int(a[1:]) for a in sorted_combo]
				if sorted_combo_nums == range(sorted_combo_nums[0],sorted_combo_nums[-1] + 1):
					run_combos.append(sorted_combo)

	return run_combos

def makeNumberSets(number_sets):
	number_combos = []
	for x in number_sets:
		for y in range(3, 5):
			for combo in combinations(x, y):
				if len(set(combo)) == len(combo):
					number_combos.append(list(combo))

	return number_combos

def makeValidPlays(individual_tiles, sets):
	plays = []
	for y in range(1, len(sets) + 1):
		# For every combination of sets that we have.
		for combo in combinations(sets, y):
			tilecopy = individual_tiles[:]
			bigcombo = []
			bigcombo_unjoined = []
			for b in combo:
				bigcombo += b
				bigcombo_unjoined.append(b)

			# Check if the combo is valid given which tiles it uses and which we have	
			try:
				for t in bigcombo:
					tilecopy.remove(t)
				plays.append(bigcombo_unjoined)
			except ValueError:
				pass

	return plays

def findBest(valid_plays):
	best_move = []
	longest = 0
	for y in valid_plays:
		length = 0
		sum = 0
		for x in y:
			length += len(x)
			for z in x:
				sum += int(z[1:])

		if sum >= 30 and length > longest:
			best_move = y
			longest = length
	return best_move

def addTile(tiles):
	bag = ['%s%i' % (i, j) for i in ['B','Y','R','P'] for j in range(1, 14)] * 2
	for item in tiles:
		bag.remove(item)
	new_tile = bag.pop(random.randrange(len(bag)))
	print new_tile
	return new_tile

def findMove(tiles):
	print "Tiles are: " + tiles
	individual_tiles = tiles.split(' ')
	sets = []
	valid_plays = []
	best_move = []
	colors_key = ['P', 'R', 'Y', 'B']
	numbers_key = range(1, 14)
	color_sets = [[] for _ in xrange(4)]
	number_sets = [[] for _ in xrange(13)]

	for tile in individual_tiles:
		# Sort tiles into 4 lists depending on what color they are.
		tile_color = colors_key.index(tile[0])
		color_sets[tile_color].append(tile)

		# Sort tiles into lists depending on what their number is.
		tile_number = numbers_key.index(int(tile[1:]))
		number_sets[tile_number].append(tile)

	# Remove empty number sets
	number_sets[:] = [x for x in number_sets if x != []]

	# Find all of the run combinations of different colors.
	for combo in makeColorSets(color_sets):
		sets.append(combo)

	# Find all of the same number groupings of different colors.
	for combo in makeNumberSets(number_sets):
		sets.append(combo)

	for play in makeValidPlays(individual_tiles, sets):
		valid_plays.append(play)

	best_move = findBest(valid_plays)
	if best_move == []:
		print "IMPOSSIBLE"
		tiles += ' ' + addTile(individual_tiles)
		findMove(tiles)
	else:
		for x in best_move: 
			print ' '.join(x)


findMove(tiles)
