from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("It's impossible to create Circle")
        self.radius = radius
        self.name = f"Circle with radius: {radius}"

    def get_area(self):
        return round(3.14 * self.radius**2, 6)

    def get_perimeter(self):
        return round(2 * 3.14 * self.radius, 4)
