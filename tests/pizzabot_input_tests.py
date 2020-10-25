import pytest

from pizzabot.pizzabot_input import PizzabotInput
from pizzabot.pizzabot_coordinates import PizzabotCoordinate, default_order


@pytest.fixture
def empty_input():
    return PizzabotInput()


@pytest.fixture
def valid_small_input():
    return PizzabotInput("5x5 (1, 3) (4, 4)")


def test_empty_input_string(empty_input):
    assert len(empty_input) == 0


def test_valid_small_input_string(valid_small_input):
    assert len(valid_small_input) == 17


def test_default_grid(valid_small_input):
    assert valid_small_input.grid.x == 0
    assert valid_small_input.grid.y == 0


def test_default_coordinates(valid_small_input):
    assert len(valid_small_input.coordinates) == 0

def test_extract_grid_coordinates(valid_small_input):
    valid_small_input.extract_grid()
    assert valid_small_input.grid.x == 5
    assert valid_small_input.grid.y == 5

def test_extract_coordinates_coordinates(valid_small_input):
    valid_small_input.extract_coordinates()
    assert len(valid_small_input.coordinates) == 2
    assert valid_small_input.coordinates[0] == \
            PizzabotCoordinate(1,3,order=default_order)
    assert valid_small_input.coordinates[1] == \
            PizzabotCoordinate(4,4,order=default_order)
