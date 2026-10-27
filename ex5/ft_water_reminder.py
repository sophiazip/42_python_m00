watered_plants: int = 0


def ft_water_reminder() -> None:
    watered_plants = int(input("Days since last watering: "))
    if (watered_plants > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
