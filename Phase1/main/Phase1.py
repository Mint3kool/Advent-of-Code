import sys
import functions

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    ops = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                ops.append(parse(line))
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(functions.countClickZero(ops, 50, 99))
    return 0

def parse(input) -> int:
    prefix = input[0]
    value = int(input[1:])
    if prefix == "L":
        return -value
    else:
        return value


if __name__ == "__main__":
    sys.exit(main())
