import sys


def main() -> None:
    name: str = sys.argv[0]
    total_argv: int = len(sys.argv)

    print("=== Command Quest ===")
    print(f"Program name: {name}")
    if total_argv == 1:
        print("No arguments provided!")
    else:
        i: int = 1
        print(f"Arguments received: {total_argv - 1}")
        for arg in sys.argv:
            if arg != "ft_command_quest.py":
                print(f"Argument {i}: {arg}")
            else:
                continue
            i += 1
    print(f"Total arguments: {total_argv}")
    print()


if __name__ == "__main__":
    main()
