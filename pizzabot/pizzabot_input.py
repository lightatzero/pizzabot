import re

from pizzabot.pizzabot_grid import PizzabotGrid

from pizzabot.pizzabot_coordinates import PizzabotCoordinate, default_order


class PizzabotInput(object):
    def __init__(self, input_string=""):
        self.input_string = input_string
        self.input_string_numbers = []
        self.grid = PizzabotGrid(0, 0)
        self.coordinates = []

    def __len__(self):
        return len(self.input_string)

    def _extract_ints(self):
        self.input_string_numbers = [int(d) for d in \
                re.findall(r'-?\d+', self.input_string)]

    def extract_grid(self):
        self._extract_ints()
        self.grid.x=self.input_string_numbers[0]
        self.grid.y=self.input_string_numbers[1]

    def extract_coordinates(self):
        self._extract_ints()
        list_of_coordinate_ints=self.input_string_numbers[2:]
        for x, y in zip(*[iter(list_of_coordinate_ints)]*2):
            self.coordinates.append(
                    PizzabotCoordinate(x,y,order=default_order))
