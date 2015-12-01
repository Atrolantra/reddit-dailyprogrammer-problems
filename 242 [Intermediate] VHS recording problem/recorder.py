from itertools import combinations

times = open('times.txt').read().splitlines()

def find_sum_in_list(numbers):
    results = []
    maxi = 0
    for x in range(1, len(numbers)):
        for combo in combinations(numbers, x):
            combo = list(combo)
            good = True
            for a in range(len(combo)):

                # if no end time is after the start time of a show following 
                # then all good
                if any(combo[a].split(' ')[1] > y.split(' ')[0] for y in combo[a+1:]):  
                    good = False
            if good:
                
                size = len(combo)  
                if size > maxi:
                    maxi = size
                    results = combo                      
    print results
    return maxi
        


combinations = find_sum_in_list(times)
print combinations

#itertools combinations
