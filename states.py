import enum as Enum

class State(object):

    symbol = '_'
    def __init__(self, cost):
        self.actions = [Actions.N, Actions.S, Actions.E, Actions.W]
        self.transitionCost = cost

        #value iteration
        self.optimalValue = 0.0
        self.vOptimalAction = '-1' #Havent found an optimal action at the beginning

    
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
        self.actions = [Actions.EXIT] 


class Boulder(State):
    symbol = 'B'
    
    def __init__(self):
        self.actions = []    


class Actions(Enum):
    N = 0
    S = 1
    E = 2
    W = 3
    EXIT = 4