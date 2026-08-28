import sys
import functions

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    sets = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                splitLine = parse(line)
                sets.extend(splitLine)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if (len(sets) == 0):
        print(f"Empty input or invalid input format. Source file path: {path}")
        return 1
    print(functions.sumBadIds(sets))
    return 0

def parse(input):
    result = []
    groups = input.rstrip('\r\n').split(",")
    # dumb input checker, I'm expecting at least "a-b,c-d"
    if (len(groups) <= 1): 
        return result

    for item in groups:
        range = item.split("-")
        result.append([range[0], range[1]])

    return result


if __name__ == "__main__":
    sys.exit(main())
