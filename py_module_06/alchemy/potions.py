from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return (
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"'{create_fire()}' and '{create_water()}'"
    )
