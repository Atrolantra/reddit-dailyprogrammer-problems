# [2015-12-28] Challenge #247 [Easy] Secret Santa
# https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/


def main():
	import random
	names = {}
	names_list = []

	for famnumber, line in enumerate(open("ssinput.txt", "r").read().splitlines()):
		family = line.split(" ")
		for member in family:
			names.update({member: famnumber})
			names_list.append(member)

	while True:
		random.shuffle(names_list)
		names_list_copy = names_list[:]
		names_list_copy.append(names_list[0])
		for x in range (len(names_list_copy) - 1):
			if names[names_list_copy[x]] == names[names_list_copy[x + 1]]:
				continue
		break

	file = open('giving.txt', 'w')
	for x in range(len(names_list_copy) - 1):
		file.write("%s gives to %s\n" % (names_list_copy[x], names_list_copy[x + 1]))


if __name__ == "__main__":
    main()
