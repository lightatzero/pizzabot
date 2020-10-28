import pytest

from pizzabot.coordinates import PizzabotCoordinate


@pytest.fixture
def simple_2d_coordinate():
    x = 3
    y = 4
    return PizzabotCoordinate(x, y)


def test_2d_point(simple_2d_coordinate):
    assert len(simple_2d_coordinate) == 2


def test_value_error(simple_2d_coordinate):
    with pytest.raises(ValueError):
        PizzabotCoordinate(1, 2, "not a int")


def test_sub(simple_2d_coordinate):
    assert simple_2d_coordinate - simple_2d_coordinate == PizzabotCoordinate(0, 0)


def test_abs(simple_2d_coordinate):
    assert int(abs(simple_2d_coordinate)) == 5
