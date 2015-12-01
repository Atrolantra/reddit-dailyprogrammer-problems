from itertools import combinations

# Fav should be set to true or false depending on if we have
# a favorite show to record in the input.
def record(fav):
    times = open('times.txt').read().splitlines()
    results = []
    maxi = 0

    if fav:
        favorite = times[0]
        shows = times[1:]

        # Get the whole entry for our fav show including times not just title.
        for z in shows:
            if (favorite in z):
                favorite = z
                shows.remove(favorite)
    else:
        shows = times

    # Brute check every combination of 1 show or more
    for x in range(1, len(shows)):
        for combo in combinations(shows, x):
            combo = list(combo)
            if fav:
                combo.append(favorite)
            combo.sort()
            # If the end time of a show prior isn't later than the start time of a show after it then we're all good.
            if not any(combo[a].split(' ')[1] > y.split(' ')[0] for a in range(len(combo)) for y in combo[a+1:]):
                if len(combo) > maxi:
                    maxi = len(combo)
                    results = combo                      

    for show in [str(' '.join(line.split(' ')[2:])) for line in results]:
        print show
    print maxi
        
record(True)
