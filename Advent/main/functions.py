# Counting numbers of zeros
import math
import time

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
            if isRepeatedNumber(value):
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

def isRepeatedNumber(front) -> bool:
    back = 0
    power = 0
    leadingZero = False
    while (front > back):
        r = front % 10
        front = front // 10
        back = back  + r * pow(10, power)

        if (r == 0 and back != 0):
            leadingZero = True
        elif (r != 0 and back != 0):
            leadingZero = False

        if (verifyRepeatedNumber(front, back, power) and not leadingZero):
            return True

        if (back == front and not leadingZero):
            return True

        power += 1

    return False

def verifyRepeatedNumber(prefix, suffix, power) -> bool:
    # print(f"{prefix}, {suffix}, {power}")
    section = []
    while (prefix > 0):
        r2 = prefix % (10 * pow(10, power))
        section.append(r2)
        prefix = prefix // (10 * pow(10, power))

    if(len(section) == 0):
        return False

    for value in section:
        if value != suffix:
            return False

    return True

def maxVoltage(batteries) -> int:
    total = 0
    for value in batteries:
        total += getBatteryVoltage(value, 12)

    return total

def getBatteryVoltage(battery) -> int:
    if battery < 11:
        raise(f"Invalid battery size, must be > 100: {battery}")

    left = 0
    right = 0
    right = battery % 10
    battery = battery // 10
    left = battery % 10
    battery = battery // 10

    # print(f"{left}, {right}")

    while battery > 0:
        r = battery % 10
        # print(f"{battery}, {r}")
        battery = battery // 10
        if (r > left):
            right = max(left, right)
            left = r
        elif(r == left):
            if left > right:
                right = r
        if (left == 9 and right == 9):
            return 99
    
    return left * 10 + right

def getBatteryVoltage(bank, size) -> int:
    voltage = 0
    batteries = []
    while bank > 0:
        r = bank % 10
        bank = bank // 10
        batteries.append(r)

    maxRange = len(batteries)
    for offset in reversed(range(size)):
        maxInRange = savedIndex = -1
        while (offset < maxRange):
            if (batteries[offset] >= maxInRange):
                maxInRange = batteries[offset]
                savedIndex = offset
            offset += 1
        voltage = voltage * 10 + maxInRange
        batteries[savedIndex] = 0
        maxRange = savedIndex
    return voltage

def countAccessibleRolls(rows) -> int:
    total = 0
    if (len(rows[1]) < 1):
        return 0

    maxLen = len(rows[1])

    ## Always using the middle row to count elements around
    for index, element in enumerate(rows[1]):
        if (element == "@"):
            l = getLower(index, 1)
            r = getHigher(index, 1, maxLen)

            segment = rows[0][l:r] + rows[1][l:r] + rows[2][l:r]
            count = segment.count("@") - 1
            
            if (count < 4):
                total += 1

    return total

def getLower(index, offset) -> int:
    if (index - offset <= 0):
        return 0
    return index - offset

def getHigher(index, offset, max) -> int:
    if (index + offset > max):
        return max
    return index + offset + 1