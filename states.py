
class State(object):

    def __init__(self, cost):
        self.actions = ["N", "S", "E", "W"]
        self.transitionCost = cost
    
    


    #toString function
    def __str__(self):
         return "State"
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        return "State"


class Terminal(State):

    def __init__(self, cost):
        super().__init__(cost)
        self.actions = ["EXIT"]    
        
    #toString function
    def __str__(self):
         return "Terminal"
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        return "Terminal"


class Boulder(State):
    
    def __init__(self):
        self.actions = []    
        
    #toString function
    def __str__(self):
         return "Boulder"
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        return "Boulder"