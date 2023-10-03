from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("side_x", "area", "perimeter"),
                         [(2, 4, 8),
                          (0.01, 0.0001, 0.04)])
def test_square_positive(side_x, area, perimeter):
    s = Square(side_x)
    assert s.name == f"Square with side {side_x}"
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_x", "area", "perimeter"),
                         [(0, 0, 0),
                          (-2, 4, -8)])
def test_square_negative(side_x, area, perimeter):
    with pytest.raises(ValueError):
        s = Square(side_x)
        assert s.name == f"Square with side {side_x}"
        assert s.get_area() == area
        assert s.get_perimeter() == perimeter


def test_add_area_positive():
    s = Square(2)
    c = Circle(3)
    r = Rectangle(2, 5)
    t = Triangle(3, 4, 5)
    assert s.add_area(c) == 32.26
    assert s.add_area(r) == 14
    assert s.add_area(t) == 10


def test_add_area_negative():
    with pytest.raises(ValueError):
        s = Square(2)
        r = 3
        assert s.add_area(r) == 38.26
