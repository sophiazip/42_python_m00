units_type: dict[str, str] = {
    "packets": "packets available",
    "grams": "grams total",
    "area": "covers {} square meters"
}


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(f'{seed_type.capitalize()} \
              seeds: {quantity} {units_type["packets"]}')
    elif (unit == "grams"):
        print(f'{seed_type.capitalize()} \
              seeds: {quantity} {units_type["grams"]}')
    elif (unit == "area"):
        area = units_type["area"].format(quantity)
        print(f'{seed_type.capitalize()} seeds: {area}')
    else:
        print("Unknown unit type")
