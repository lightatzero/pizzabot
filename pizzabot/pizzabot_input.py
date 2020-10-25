from pizzabot.pizzabot_grid import PizzabotGrid

class PizzabotInput(object):
    def __init__(self, input_string=""):
        self.input_string = input_string 
        self.grid = PizzabotGrid(0,0) 

    def __len__(self):
        return len(self.input_string)
