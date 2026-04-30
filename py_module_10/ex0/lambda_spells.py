# flake8: noqa: E731

artifact_sorter = lambda artifacts: sorted(
    artifacts,
    key=lambda artifact: artifact["power"],
    reverse=True
)

power_filter = lambda mages, min_power: [
    *filter(
        lambda mage: mage["power"] >= min_power,
        mages
    )
]

spell_transformer = lambda spells: [
    *map(
        lambda spell: "*" + spell + "*",
        spells
    )
]

mage_stats = lambda mages: {
    "max_power": max(map(lambda mage: mage["power"], mages)),
    "min_power": min(map(lambda mage: mage["power"], mages)),
    "avg_power": round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2
    )
}


artifacts = [
    {"name": "Crystal Orb", "power": 85, "type": "orb"},
    {"name": "Fire Staff", "power": 92, "type": "staff"},
    {"name": "Ancient Tome", "power": 70, "type": "book"}
]

mages = [
    {"name": "Sage Lambda", "power": 95, "element": "light"},
    {"name": "Mage Filter", "power": 60, "element": "water"},
    {"name": "Wizard Map", "power": 75, "element": "fire"}
]

spells = [
    "fireball",
    "heal",
    "shield"
]


print("Testing artifact_sorter...")
sorted_artifacts = artifact_sorter(artifacts)
print(
    sorted_artifacts[0]["name"],
    "(" + str(sorted_artifacts[0]["power"]) + " power)",
    "comes before",
    sorted_artifacts[1]["name"],
    "(" + str(sorted_artifacts[1]["power"]) + " power)"
)

print()
print("Testing spell_transformer...")
print(spell_transformer(spells))