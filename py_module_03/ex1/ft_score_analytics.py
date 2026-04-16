import sys


def main() -> None:
    print("===  Player Score Analytics ===")
    count: int = len(sys.argv)
    if (count > 1):
        i: int = 1
        list_arg = ""
        while (count > i):
            list_arg += sys.argv[i]
            if i < count - 1:
                list_arg += ", "
            i += 1

        print(f"Scores processed: [{list_arg}]")
    else:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> "
              "<score2> ...")


if __name__ == "__main__":
    main()
