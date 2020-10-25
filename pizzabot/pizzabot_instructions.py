from dataclasses import dataclass, field
from typing import List

from pizzabot.pizzabot_coordinates import PizzabotCoordinate as DeltaCord
from pizzabot.pizzabot_coordinates import default_order

shorthand_description_movement = [
    ("N", "Move north", DeltaCord(1, 0, order=default_order)),
    ("S", "Move south", DeltaCord(-1, 0, order=default_order)),
    ("E", "Move east", DeltaCord(0, 1, order=default_order)),
    ("W", "Move west", DeltaCord(0, -1, order=default_order)),
    ("D", "Drop pizza", DeltaCord(0, 0, order=default_order)),
]


@dataclass
class Instruction:
    shorthand: str
    description: str
    movement: DeltaCord


def make_instructions():
    return [Instruction(s, d, m) for s, d, m in shorthand_description_movement]


@dataclass
class PizzabotInstructions:
    Instructions: List[Instruction] = field(default_factory=make_instructions)
