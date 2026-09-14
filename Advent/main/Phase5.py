import sys
import functions
import re

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    idRanges = []
    inputIds = []
    count = 0
    sumOfGoodFood = 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            lineNumber = 0
            for line in f:
                line = re.sub(r'\s+', ' ', line).strip()
                if "-" in line:
                    newRange = line.split("-")
                    idRanges = functions.combineRanges(idRanges,[int(newRange[0]), int(newRange[1])])
                else:
                    if len(line) > 0:
                        inputIds.append(int(line))

            for id in inputIds:
                if functions.inRanges(idRanges, id):
                    count += 1

            print(idRanges)

            for range in idRanges:
                minVal = min(range[0], range[1])
                maxVal = max(range[0], range[1])
                sumOfGoodFood += maxVal - minVal + 1
                    
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    
    print(f"Fresh: {count}")
    print(f"ValidIds: {sumOfGoodFood}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
