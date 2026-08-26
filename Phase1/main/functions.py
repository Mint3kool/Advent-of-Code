# Counting numbers of zeros
def countZeros(arr, start, max) -> int:
    count = 0
    for value in arr:
        start = add(start, value, max)
        if start == 0:
            count += 1

    return count

def countClickZero(arr, start, max) -> int:
    count = 0
    # print("init: " + str(start))
    for value in arr:
        count += clickZero(start, value, max)
        start = add(start, value, max)

    return count

def clickZero(start, increment, max) -> int:
    count = 0

    if abs(increment) > max:
        rotations = abs(increment) // (max + 1)
        count += rotations
    remainder = (abs(increment) % (max + 1))
    if (increment < 0):
        remainder = -remainder
    if (start + remainder > max):
        count += 1
    elif (start + remainder <= 0 and start != 0):
        count += 1

    return count

# Values start @ 0
def add(first, second, max) -> int:
    sum = first + (second % (max + 1))

    if (sum > max):
        sum = sum - (max + 1)
    elif (sum < 0):
        sum = sum + max

    return sum

