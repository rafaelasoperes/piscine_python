import random


def gen_player_achievements() -> set:
    achievements_pool = (
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Hidden Path Finder",
        "Boss Slayer",
    )

    amount = random.randint(5, 10)
    picked = random.sample(achievements_pool, amount)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===")

    player_names = ("Alice", "Bob", "Charlie", "Dylan")

    players = {}
    i = 0
    while i < len(player_names):
        players[player_names[i]] = gen_player_achievements()
        i += 1

    i = 0
    while i < len(player_names):
        name = player_names[i]
        print(f"Player {name}: {players[name]}")
        i += 1

    all_distinct: set = set()
    i = 0
    while i < len(player_names):
        all_distinct = all_distinct.union(players[player_names[i]])
        i += 1
    print()
    print(f"All distinct achievements: {all_distinct}")

    common = players[player_names[0]]
    i = 1
    while i < len(player_names):
        common = common.intersection(players[player_names[i]])
        i += 1
    print()
    print(f"Common achievements: {common}")

    print()
    i = 0
    while i < len(player_names):
        current_name = player_names[i]
        others: set = set()

        j = 0
        while j < len(player_names):
            if j != i:
                others = others.union(players[player_names[j]])
            j += 1

        unique_only = players[current_name].difference(others)
        print(f"Only {current_name} has: {unique_only}")
        i += 1

    print()
    i = 0
    while i < len(player_names):
        current_name = player_names[i]
        missing = all_distinct.difference(players[current_name])
        print(f"{current_name} is missing: {missing}")
        i += 1


if __name__ == "__main__":
    main()
