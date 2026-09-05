length: int = 0
width: int = 0
area: int = 0


def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f'Plot area: {area}')
