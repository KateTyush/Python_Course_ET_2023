from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("side_x", "side_y", "area", "perimeter"),
                         [(2, 3, 6, 10),
                          (0.01, 0.01, 0.0001, 0.04)])
def test_rectangle_positive(side_x, side_y, area, perimeter):
    r = Rectangle(side_x, side_y)
    assert r.name == f"Rectangle with sides: {side_x} and {side_y}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_x", "side_y", "area", "perimeter"),
                         [(0, 3, 0, 6),
                          (0, 0, 0, 0),
                          (-10, -10, 100, -40),
                          (-1, 10, -10, 18)])
def test_rectangle_negative(side_x, side_y, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_x, side_y)
        assert r.name == f"Rectangle with sides: {side_x} and {side_y}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


def test_add_area_positive():
    r = Rectangle(2, 5)
    s = Square(3)
    t = Triangle(3, 4, 5)
    c = Circle(2)
    assert r.add_area(s) == 19
    assert r.add_area(t) == 16
    assert r.add_area(c) == 22.56


def test_add_area_negative():
    with pytest.raises(ValueError):
        r = Rectangle(2, 5)
        s = 5
        assert r.add_area(s) == 19
