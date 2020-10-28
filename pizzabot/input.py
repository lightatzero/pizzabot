import re

from pizzabot.grid import PizzabotGrid
from pizzabot.coordinates import PizzabotCoordinate


class PizzabotInput(object):
    def __init__(self, input_string=""):
        self.input_string = input_string
        self.input_string_numbers = []
        self.grid = PizzabotGrid(0, 0)
        self.coordinates = []
        self._extract_ints()
        if len(self.input_string_numbers) >= 2:
            self.extract_grid()
            self.extract_coordinates()

    def __len__(self):
        return len(self.input_string)

    def _extract_ints(self):
        self.input_string_numbers = [
            int(d) for d in re.findall(r"-?\d+", self.input_string)
        ]

    def extract_grid(self):
        self.grid = PizzabotGrid(0, 0)
        self.grid.x = self.input_string_numbers[0]
        self.grid.y = self.input_string_numbers[1]

    def extract_coordinates(self):
        self.coordinates = []
        list_of_coordinate_ints = self.input_string_numbers[2:]
        for x, y in zip(*[iter(list_of_coordinate_ints)] * 2):
            self.coordinates.append(PizzabotCoordinate(x, y))
