from pizzabot.input import PizzabotInput
from pizzabot.coordinates import PizzabotCoordinate, default_order
from pizzabot.instructions import PizzabotInstructions


class PizzabotEngine(object):
    def __init__(self):
        self.instructions = PizzabotInstructions().Instructions
        self.position = PizzabotCoordinate(0, 0, order=default_order)
        self.journey = []
        self.input = None

    def update_postion(self, target):
        init_delta = (target - self.position).norm(order=2)
        for instruction in self.instructions:
            delta = (target - instruction.movement - self.position).norm(order=2)
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
