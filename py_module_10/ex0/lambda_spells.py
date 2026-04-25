def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(sum(map
                               (lambda m: m['power'], mages)) / len(mages), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Blade', 'power': 70, 'type': 'blade'},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before {sorted_artifacts[1]['name']}"
        f" ({sorted_artifacts[1]['power']} power)"
    )

    mages = [
        {'name': 'Alex', 'power': 90, 'element': 'fire'},
        {'name': 'Jordan', 'power': 40, 'element': 'water'},
        {'name': 'Riley', 'power': 75, 'element': 'earth'},
    ]

    filtered = power_filter(mages, 70)
    print(f"\nFiltered mages (power >= 70): {[m['name'] for m in filtered]}")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    print("\nMage stats:")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']},"
          f" Avg: {stats['avg_power']}")
