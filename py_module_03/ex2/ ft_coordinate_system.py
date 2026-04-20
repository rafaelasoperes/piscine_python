import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            lines: str = input("Enter new coordinates as "
                               "floats in format 'x,y,z': ")

            parts = []
            current_part = ""

            for char in lines:
                if char == ",":
                    parts += [current_part]
                    current_part = ""
                elif char != " ":
                    current_part += char
            parts += [current_part]

            if len(parts) != 3 or parts[0] == "":
                print("Invalid syntax")
                continue

            floats: list[float] = []
            for p in parts:
                try:
                    floats += [float(p)]
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
                    raise

            return (floats[0], floats[1], floats[2])

        except ValueError:
            continue


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")
    print()

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()


# A Distância Euclidiana é, de forma simples, a medida da linha reta que
# conecta dois pontos em um espaço. É a distância "como o corvo voa",
# sem curvas ou desvios.
# Ela é baseada no famoso Teorema de Pitágoras. Se você imaginar dois
# pontos em um gráfico, a distância entre eles pode ser vista como a
# hipotenusa de um triângulo retângulo.
