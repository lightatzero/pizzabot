from dataclasses import dataclass, field
from typing import List

shorthand_action_dict = {
"N": "Move north",
"S": "Move south",
"E": "Move east",
"W": "Move west",
"D": "Drop pizza",
}

@dataclass
class Instruction:
    shorthand: str
    action: str

def make_instructions():
    return [Instruction(shorthand, action) for shorthand, action in shorthand_action_dict.items()]

@dataclass
class PizzabotInstructions:
    Instructions: List[Instruction] = field(default_factory=make_instructions)
