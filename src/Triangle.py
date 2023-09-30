from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("It's impossible to create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle with sides: {side_a}, {side_b}, {side_c}"

    def get_area(self):
        p = 0.5 * (self.side_a + self.side_b + self.side_c)
        return round((p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))**0.5, 5)

    def get_perimeter(self):
        return round(self.side_a + self.side_b + self.side_c, 4)
