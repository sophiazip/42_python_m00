day_1: int = 0
day_2: int = 0
day_3: int = 0
total_harvest: int = 0


def ft_harvest_total() -> None:
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    total_harvest = day_1 + day_2 + day_3
    print(f'Total harvest: {total_harvest}')
