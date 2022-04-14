
class Agent():

    def __init__(self,grid):
        self.grid = grid
        self.score = 0
    
    def act(self, startX, startY):
        currState = self.grid[startX][startY]

        done = False
        while(not done):
            self.score += currState.transitionCost

            currState = currState.decide()
            if currState is Transition:
                done = True

        print("final score is " + self.score)
        #Update state values for next run through?
            

