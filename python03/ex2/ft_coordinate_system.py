import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            x_text, y_text, z_text = user_input.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_text)
        except ValueError:
            print(
                f"Error on parameter '{x_text}': "
                f"could not convert string to float: '{x_text}'"
            )
            continue

        try:
            y = float(y_text)
        except ValueError:
            print(
                f"Error on parameter '{y_text}': "
                f"could not convert string to float: '{y_text}'"
            )
            continue

        try:
            z = float(z_text)
        except ValueError:
            print(
                f"Error on parameter '{z_text}': "
                f"could not convert string to float: '{z_text}'"
            )
            continue

        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_position = get_player_pos()

    print(f"Got a first tuple: {first_position}")
    print(
        f"It includes: X={first_position[0]}, "
        f"Y={first_position[1]}, Z={first_position[2]}"
    )
    center_distance = math.sqrt(
        first_position[0] ** 2
        + first_position[1] ** 2
        + first_position[2] ** 2
    )
    print(f"Distance to center: {round(center_distance, 4)}")

    print("\nGet a second set of coordinates")
    second_position = get_player_pos()
    position_distance = math.sqrt(
        (second_position[0] - first_position[0]) ** 2
        + (second_position[1] - first_position[1]) ** 2
        + (second_position[2] - first_position[2]) ** 2
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(position_distance, 4)}"
    )
 # not: Koordinat sistemi x ve y değerlerini birlikte taşıyan bir veri yapısıdır.
