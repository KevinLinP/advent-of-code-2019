import multiprocessing

def is_valid(num):
    places = map(int, list(str(num)))
    places = list(places)
    same_adjacent = False

    for i in range(1, 6):
        if places[i-1] > places[i]:
            return False
        if not same_adjacent:
            if (places[i-1] == places[i] and 
                ((i == 1) or (places[i-2] != places[i])) and 
                ((i == 5) or (places[i+1] != places[i]))):

                same_adjacent = True

    return same_adjacent

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    start = 171309
    end = 643603

    results = pool.map(is_valid, range(start, end+1))
    pool.close()

    print(results.count(True))
