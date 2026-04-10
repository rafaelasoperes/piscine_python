def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    type = seed_type.capitalize()
    if unit == "packets":
        print(f"{type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
