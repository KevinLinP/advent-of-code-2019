def is_valid(num):
    places = map(int, list(str(num)))
    same_adjacent = False

    for i in range(1, 6):
        if places[i-1] > places[i]:
            return False
        if not same_adjacent:
            if places[i-1] == places[i]:
                same_adjacent = True
                if (i > 1) and (places[i-2] == places[i]):
                    same_adjacent = False

                if (i < 5) and (places[i+1] == places[i]):
                    same_adjacent = False

    return same_adjacent

def something(start, end):
    num_valid = 0

    for n in range(start, end + 1):
        if is_valid(n):
            num_valid += 1

    return num_valid

print(something(171309, 643603))
