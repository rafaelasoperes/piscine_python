import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    initial_players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized: list[str] = [
        name.capitalize() for name in initial_players
    ]
    print(f"New list with all names capitalized: {all_capitalized}")

    originally_cap: list[str] = [
        name for name in initial_players if name.istitle()
    ]
    print(f"New list of capitalized names only: {originally_cap}\n")

    scores: dict[str, int] = {
        name: random.randint(50, 1000) for name in all_capitalized
    }
    print(f"Score dict: {scores}")

    total: int = 0
    for name in scores:
        total += scores[name]

    average: float = total / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores: dict[str, int] = {}
    for name in scores:
        if scores[name] > average:
            high_scores[name] = scores[name]

    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
