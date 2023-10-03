from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(2, 4, 5, 3.79967, 11),
                          (0.1, 0.1, 0.1, 0.00433, 0.3)])
def test_triangle_positive(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle with sides: {side_a}, {side_b}, {side_c}"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(0, 3, 4, 0, 7),
                          (0, 0, 0, 0, 0),
                          (2, 0, 0, 0, 2),
                          (-10, -10, -5, 0, -25),
                          (-1, 10, 10, -10, 19),
                          (1, 2, 3, 0, 6),
                          (7, 2, 3, 0, 6)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)
        assert t.name == f"Triangle with sides: {side_a}, {side_b}, {side_c}"
        assert t.get_area() == area
        assert t.get_perimeter() == perimeter


def test_add_area_positive():
    t = Triangle(2, 4, 5)
    s = Square(2)
    r = Rectangle(2, 5)
    c = Circle(3)
    assert t.add_area(s) == 7.8
    assert t.add_area(r) == 13.8
    assert t.add_area(c) == 32.06


def test_add_area_negative():
    with pytest.raises(ValueError):
        t = Triangle(2, 5, 5)
        s = 5
        assert t.add_area(s) == 19
