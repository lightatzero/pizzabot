import re

from pizzabot.grid import PizzabotGrid
from pizzabot.coordinates import PizzabotCoordinate


INPUT_STRING_START_WITH_GRID_REGEX = r"^-?\dx-?\d \("
GET_ALL_INTEGERS_REGEX = r"-?\d+"
BEGINS_AND_ENDS_WITH_BRACKET = r"^\(.*\)$"
COORDINATES_WITHOUT_BRACKET = r"^-?\d\,\ ?-?\d$"


class PizzabotInput(object):
    def __init__(self, input_string=""):
        self.input_string = ""
        self.input_string_numbers = []
        self.coordinates = []
        self.grid = PizzabotGrid(0, 0)
        if self._validate_input_string(input_string):
            self._extract_ints()
            self.extract_grid()
            self.extract_coordinates()

    def __len__(self):
        return len(self.input_string)

    def _validate_input_string(self, input_string):
        if re.match(INPUT_STRING_START_WITH_GRID_REGEX, input_string) == None:
            return False
        cord_input_string = input_string.split(" ", 1)[1]
        if re.match(BEGINS_AND_ENDS_WITH_BRACKET, cord_input_string) == None:
            return False
        cord_input_string = cord_input_string[1:-1]
        cords_list = cord_input_string.split(") (")
        for cord in cords_list:
            if re.match(COORDINATES_WITHOUT_BRACKET, cord) == None:
                return False
        self.input_string = input_string
        return True

    def _extract_ints(self):
        self.input_string_numbers = [
            int(d) for d in re.findall(GET_ALL_INTEGERS_REGEX, self.input_string)
        ]

    def extract_grid(self):
        self.grid = PizzabotGrid(0, 0)
        if len(self.input_string_numbers) >= 2:
            self.grid.x = self.input_string_numbers[0]
            self.grid.y = self.input_string_numbers[1]

    def extract_coordinates(self):
        self.coordinates = []
        list_of_coordinate_ints = self.input_string_numbers[2:]
        for x, y in zip(*[iter(list_of_coordinate_ints)] * 2):
            self.coordinates.append(PizzabotCoordinate(x, y))
