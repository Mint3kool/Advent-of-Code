# Counting numbers of zeros
import math
import time
import numpy as np

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

def maxVoltage(bank) -> int:
    total = 0
    for batteries in bank:
        total += getBatteryVoltage(batteries, 12)

    return total

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

def removeRollsFromBacklog(backlog, loadedLines) -> int:
    total_removed = 0
    while (len(backlog) > 0):
        # print(backlog)
        target_row = backlog.pop(0)
        input_line = loadedLines[target_row]
        adjLines = getAdjacentRows(target_row, loadedLines)
        output_line = removeAccessibleRolls(adjLines)
        # print(input_line)
        initCount = input_line.count("@")
        finalCount = output_line.count("@")
        total_removed += initCount - finalCount
        if (input_line != output_line):
            if (target_row > 0):
                backlog.append(target_row - 1)
            backlog.append(target_row)
            loadedLines[target_row] = output_line

    return total_removed


def getAdjacentRows(targetLineNum, context):
    top = bottom = ""
    target = context[targetLineNum]
    if (targetLineNum - 1 in context):
        top = context[targetLineNum - 1]
    if (targetLineNum + 1 in context):
        bottom = context[targetLineNum + 1]
    return [top, target, bottom]

def removeAccessibleRolls(rows) -> str:
    maxLen = len(rows[1])
    middle = list(rows[1])

    # print(f"{len(rows[0])} ; {len(rows[1])} ; {len(rows[2])}")
    # print(f"{rows[0]} ; {rows[1]} ; {rows[2]}")
    if(len(rows[0]) == 0 and len(rows[2]) == 0):
        print("skipped")
        return rows[1]

    ## Always using the middle row to count elements around
    for index, element in enumerate(rows[1]):
        l = 0 if index - 1 <= 0  else index - 1
        r = maxLen if index + 1 > maxLen else index + 1 + 1

        segment = rows[0][l:r] + "".join(middle)[l:r] + rows[2][l:r]
        if (canRemoveRoll(segment, element)):
            middle[index] = "."
        # print(middle)

    return "".join(middle)

def countAccessibleRolls(rows) -> int:
    total = 0
    if (len(rows[1]) < 1):
        return 0

    maxLen = len(rows[1])

    ## Always using the middle row to count elements around
    for index, element in enumerate(rows[1]):
        if (element == "@"):
            l = 0 if index - 1 <= 0  else index - 1
            r = maxLen if index + 1 > maxLen else index + 1 + 1

            segment = rows[0][l:r] + rows[1][l:r] + rows[2][l:r]
            count = segment.count("@") - 1

            if (count < 4):
                total += 1

    return total

def canRemoveRoll(segment, element) -> bool:
    if (element != "@"):
        return False
    
    count = segment.count("@") - 1

    if (count < 4):
        return True

    return False

def inRanges(idRanges, inputId) -> bool:
    for ids in idRanges:
        minVal = min(ids[0], ids[1])
        maxVal = max(ids[0], ids[1])
        if inputId >= minVal and inputId <= maxVal:
            return True

    return False

def inRange(idRange, inputId) -> bool:
    minVal = min(idRange[0], idRange[1])
    maxVal = max(idRange[0], idRange[1])
    if inputId >= minVal and inputId <= maxVal:
        return True

    return False

def combineRanges(idRanges, newRange):
    minNewVal = min(newRange[0], newRange[1])
    maxNewVal = max(newRange[0], newRange[1])

    newSets = []

    if (len(idRanges) == 0):
        idRanges.append([minNewVal, maxNewVal])
        return idRanges

    index = 0
    while index < len(idRanges):
        if (inRange(idRanges[index], minNewVal) or inRange(idRanges[index], maxNewVal)
            or inRange([minNewVal, maxNewVal], idRanges[index][0]) or inRange([minNewVal, maxNewVal], idRanges[index][1])):
            # found = True
            minNewVal = min(minNewVal, idRanges[index][0], idRanges[index][1])
            maxNewVal = max(maxNewVal, idRanges[index][0], idRanges[index][1])
            newSets.append([minNewVal, minNewVal])
            idRanges.pop(index)
        else:
            index = index + 1

        # print(f"{idRanges}| {minNewVal}, {maxNewVal}")
  
    idRanges.append([minNewVal, maxNewVal])

    return idRanges

def workOnSplitLine(input) -> int:
    operations = input.pop()
    currentOp = ""
    arr = np.array(input)
    result = np.where(arr == ' ', '0', arr).astype(int)

    runningTotal = 0
    rowTotal = 0

    for index, value in enumerate(input[0]):
        currentValue = 0
        power = 0

        if (len(operations) > 0 and operations[0] != " "):
            currentOp = operations.pop(0)
        else:
            if len(operations) > 0:
                operations.pop(0)
        
        for value in result[:,index]:
            if (value > 0):
                currentValue = currentValue * 10
                currentValue += value
                
                power += 1

        # print(currentValue)
        # print(currentOp)

        if (currentValue != 0):
            if rowTotal == 0:
                rowTotal = currentValue
            else:
                rowTotal = basicCalculate(rowTotal, currentValue, currentOp)
        else:
            print(f"rt: {rowTotal}")
            runningTotal += rowTotal
            rowTotal = 0
            currentOp = ""

    if rowTotal > 0:
        runningTotal = basicCalculate(runningTotal, rowTotal, "+")
    
    return runningTotal

def basicCalculate(first, second, operation) -> int:
    match operation:
        case "+":
            return first + second
        case "*":
            return first * second

def findSumTotal(input) -> int:
    total = 0
    ops = input.pop()
    arr = np.array(input, dtype=int)

    for index, value in enumerate(ops):
        match value:
            case "+":
                total += np.sum(arr[:, index])
            case "*":
                total += np.prod(arr[:, index])
    return total