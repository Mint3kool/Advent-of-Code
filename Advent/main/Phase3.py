import sys
import functions

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    batteries = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                batteries.append(int(line))
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(functions.maxVoltage(batteries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
