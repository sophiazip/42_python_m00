until_harvest: int = 0


def ft_count_harvest_iterative() -> None:
    until_harvest = int(input("Days until harvest: "))
    for i in range(until_harvest + 1):
        print(f'Day {i}')
    print("Harvest time!")
