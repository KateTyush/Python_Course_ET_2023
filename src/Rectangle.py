from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_x, side_y):
        super().__init__()
        if side_x <= 0 or side_y <= 0:
            raise ValueError("It's impossible to create Rectangle")
        self.side_x = side_x
        self.side_y = side_y
        self.name = f"Rectangle with sides: {side_x} and {side_y}"

    def get_area(self):
        return self.side_x * self.side_y

    def get_perimeter(self):
        return 2 * (self.side_x + self.side_y)
