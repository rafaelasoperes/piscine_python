import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    count: int = len(sys.argv)
    if (count > 1):
        print(f"Arguments received: {count - 1}")
        i: int = 1
        while (i < count):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    else:
        print("No arguments provided!")

    print(f"Total arguments: {count}")


if __name__ == "__main__":
    main()
