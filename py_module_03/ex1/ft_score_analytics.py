import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args: list[str] = sys.argv[1:]
    valid_scores: list[int] = []

    for arg in args:
        try:
            score = int(arg)
            valid_scores += [score]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not valid_scores:
        script_name = sys.argv[0]
        print(f"No scores provided. Usage: python3 "
              f"{script_name} <score1> <score2> ...")
        return
    else:
        total_players: int = len(valid_scores)
        total_score: int = sum(valid_scores)
        average: float = total_score / total_players
        high: int = max(valid_scores)
        low: int = min(valid_scores)
        score_range: int = high - low

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")
    print()


if __name__ == "__main__":
    main()
