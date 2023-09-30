from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_x):
        if side_x <= 0:
            raise ValueError("It's impossible to create Square")
        super().__init__(side_x, side_x)
        self.side_x = side_x
        self.name = f"Square with side {side_x}"
