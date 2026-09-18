import sys
import functions
import re

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]

    fullSet = []

    try:
        parent = ["",0]
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                input = line.strip("\n")
                fullSet.append(input)
                parent = functions.splitBeams(parent, input)

        print(f"end: {parent}")

        result = functions.splitBeamsButQuantum(fullSet, -1)
        print(result)

    
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    
    # print(sumTotal)
    return 0

if __name__ == "__main__":
    sys.exit(main())
