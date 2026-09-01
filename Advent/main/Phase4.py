import sys
import functions

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    context = [""] * 3
    total_rolls = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                context.pop(0)
                context.append(line.rstrip('\r\n'))
                total_rolls += functions.countAccessibleRolls(context)
                # if len(context) == 3:
                #     context.pop(0)
        context.pop(0)
        context.append("")
        total_rolls += functions.countAccessibleRolls(context)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(total_rolls)
    return 0


if __name__ == "__main__":
    sys.exit(main())
