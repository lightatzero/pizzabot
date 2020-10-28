import pytest

from pizzabot.input import PizzabotInput
from pizzabot.coordinates import PizzabotCoordinate


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


def test_extract_grid_coordinates(valid_small_input):
    valid_small_input.extract_grid()
    assert valid_small_input.grid.x == 5
    assert valid_small_input.grid.y == 5


def test_extract_coordinates_coordinates(valid_small_input):
    valid_small_input.extract_coordinates()
    assert len(valid_small_input.coordinates) == 2
    assert valid_small_input.coordinates[0] == PizzabotCoordinate(1, 3)
    assert valid_small_input.coordinates[1] == PizzabotCoordinate(4, 4)


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
    pb.extract_coordinates()
    assert len(pb.coordinates) == number_of_cordinates


@pytest.mark.parametrize(
    "input_string,is_valid",
    [
        (
            "5x5!(0, 0) (1, 3) (4, 4)",
            False,
        ),
        (
            "5x5 (0, 0| (1, 3) (4, 4)",
            False,
        ),
        (
            "5x5 (1, 3) (4, 4)",
            True,
        ),
    ],
)
def test_validate_input_string(input_string, is_valid):
    pb = PizzabotInput("")
    assert pb._validate_input_string(input_string) == is_valid
