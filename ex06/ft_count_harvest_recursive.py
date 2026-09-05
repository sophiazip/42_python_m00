def _helper_harvest(harvest_days: int, until_harvest: int = 0) -> None:
    if (until_harvest <= harvest_days):
        print(f'Day {until_harvest}')
        _helper_harvest(harvest_days, until_harvest + 1)


def ft_count_harvest_recursive() -> int:
    harvest_days = int(input("Days until harvest: "))
    _helper_harvest(harvest_days)
    print("Harvest time!")
