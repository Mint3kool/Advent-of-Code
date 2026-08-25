# Counting numbers of zeros
def count(arr, start, max) -> int:
    count = 0
    for value in arr:
        start = add(start, value, max)
        if start == 0:
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

