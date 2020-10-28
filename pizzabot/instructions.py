from dataclasses import dataclass, field
from typing import List

from pizzabot.coordinates import PizzabotCoordinate as DeltaCord

shorthand_description_movement = [
    ("D", "Drop pizza", DeltaCord(0, 0)),
    ("N", "Move north", DeltaCord(0, 1)),
    ("S", "Move south", DeltaCord(0, -1)),
    ("E", "Move east", DeltaCord(1, 0)),
    ("W", "Move west", DeltaCord(-1, 0)),
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
