# Counting numbers of zeros
import math

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

def sumBadIds(sets) -> int:
    result = 0
    for set in sets:
        for value in range(int(set[0]), int(set[1]) + 1):
            if isDoubleNumber(value):
                # print(value)
                result += value
    return result

def isDoubleNumber(front) -> bool:
    back = 0
    power = 0
    leadingZero = False
    while (front > back):
        # print(f"1: f: {front} b:{back}")
        r = front % 10
        front = front // 10
        back = back  + r * pow(10, power)
        power += 1
        if (r == 0 and back != 0):
            leadingZero = True
        elif (r != 0 and back != 0):
            leadingZero = False
        # print(f"            2: f: {front} b:{back} p:{power}")
        if (back == front and not leadingZero):
            return True

    return False