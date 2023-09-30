from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from src.Circle import Circle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(2, 12.56, 12.56),
                          (0.01, 0.000314, 0.0628)])
def test_circle_positive(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == f"Circle with radius: {radius}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(0, 0, 0),
                          (-2, 12.56, -12.56)])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert c.name == f"Circle with radius: {radius}"
        assert c.get_area() == area
        assert c.get_perimeter() == perimeter


def test_add_area_positive():
    c = Circle(3)
    r = Rectangle(2, 5)
    s = Square(2)
    t = Triangle(3, 4, 5)
    assert c.add_area(r) == 38.26
    assert c.add_area(s) == 32.26
    assert c.add_area(t) == 34.26


def test_add_area_negative():
    with pytest.raises(ValueError):
        c = Circle(3)
        r = 3
        assert c.add_area(r) == 38.26
