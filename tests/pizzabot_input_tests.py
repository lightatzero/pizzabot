import pytest

from pizzabot.input import PizzabotInput
from pizzabot.coordinates import PizzabotCoordinate


@pytest.fixture
def empty_input():
    return PizzabotInput()


@pytest.fixture
def valid_small_input():
    return PizzabotInput("5x5 (1, 3) (4, 4)")


def test_extract_coordinates_coordinates(valid_small_input):
    assert len(valid_small_input.coordinates) == 2
    assert valid_small_input.coordinates[0] == PizzabotCoordinate(1, 3)
    assert valid_small_input.coordinates[1] == PizzabotCoordinate(4, 4)


def test_extract_grid_coordinates(valid_small_input):
    assert valid_small_input.grid.x == 5
    assert valid_small_input.grid.y == 5


@pytest.mark.parametrize(
    "input_string,number_of_cordinates",
    [
        (
            "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)",
            9,
        ),
        ("5x5 (1, 3) (4, 4)", 2),
    ],
)
def test_extract_coordinates_coordinates_count(input_string, number_of_cordinates):
    pb = PizzabotInput(input_string)
    assert len(pb.coordinates) == number_of_cordinates


@pytest.mark.parametrize(
    "input_string,valid_coordinates_count",
    [
        (
            "5x5!(0, 0) (1, 3) (4, 4)",
            3,
        ),
        (
            "5x5 (0, 0| (1, 3) (4, 4)",
            0,
        ),
        (
            "5x5 (1, 3)(4, 4)",
            2,
        ),
        (
            "5x5 0, 0) (1, 3) (4, 4)",
            0,
        ),
    ],
)
def test_valid_input_strings(input_string, valid_coordinates_count):
    pb = PizzabotInput(input_string)
    assert len(pb.coordinates) == valid_coordinates_count
