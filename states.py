
class State(object):
    symbol = '_'
    def __init__(self, cost):
        self.actions = ["N", "S", "E", "W"]
        self.transitionCost = cost
    
    #toString function
    def __str__(self):
         return self.symbol
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        return self.symbol


class Terminal(State):
    symbol = 'T'

    def __init__(self, cost):
        super().__init__(cost)
        self.actions = ["EXIT"] 


class Boulder(State):
    symbol = 'B'
    
    def __init__(self):
        self.actions = []

class Robot(State):
    symbol = 'R'
    
    def __init__(self):
        self.actions = []    