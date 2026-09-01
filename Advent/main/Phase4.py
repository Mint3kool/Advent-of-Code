import sys
import functions

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    loadedLines = {}
    backlog = []
    total_rolls = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            lineNumber = 0
            for line in f:
                loadedLines[lineNumber] = line.rstrip('\r\n')
                backlog.append(lineNumber)
                lineNumber += 1

        removeCount = functions.removeRollsFromBacklog(backlog, loadedLines)
        while (removeCount > 0):
            # print(removeCount)
            total_rolls += removeCount
            for index in range(len(loadedLines)):
                backlog.append(index)
            removeCount = functions.removeRollsFromBacklog(backlog, loadedLines)

        # for index in range(lineNumber):
        #     print(f"{index} \t {loadedLines[index]}")
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(total_rolls)
    return 0

if __name__ == "__main__":
    sys.exit(main())
