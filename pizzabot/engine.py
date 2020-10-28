from pizzabot.input import PizzabotInput
from pizzabot.coordinates import PizzabotCoordinate
from pizzabot.instructions import PizzabotInstructions


class PizzabotEngine(object):
    def __init__(self):
        self.instructions = PizzabotInstructions().Instructions
        self.position = PizzabotCoordinate(0, 0)
        self.journey = []
        self.input = None

    def update_postion(self, target):
        init_delta = abs(target - self.position)
        for instruction in self.instructions:
            delta = abs(target - instruction.movement - self.position)
            if delta < init_delta:
                best_instruction = instruction
        self.journey.append(best_instruction)
        self.position += best_instruction.movement
        return best_instruction

    def process_string(self, input_string):
        self.input = None
        self.input = PizzabotInput(input_string)
        for target in self.input.coordinates:
            while self.position != target:
                self.update_postion(target)
            self.journey.append(self.instructions[0])
        output_string = ""
        for step in self.journey:
            output_string += step.shorthand
        return output_string
