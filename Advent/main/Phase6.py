import sys
import functions
import re

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    values = []
    splitLine = []

    sumTotal = 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            lineNumber = 0
            for line in f:
                splitLine.append(list(line.strip("\n")))
                line = re.sub(r'\s+', ' ', line).strip()
                values.append(line.split(" "))

        print(functions.workOnSplitLine(splitLine))

        sumTotal = functions.findSumTotal(values)
        
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    
    print(sumTotal)
    return 0

if __name__ == "__main__":
    sys.exit(main())
