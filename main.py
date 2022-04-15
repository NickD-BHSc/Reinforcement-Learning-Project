import sys
from turtle import right
from states import State, Boulder, Terminal
from grid import Grid, setupGrid


def bellman(state, grid, x, y):
    
    maxValue = 0
    bestAction = 'N' #default to N
    if state.symbol == 'T':
        maxValue = state.cost
        bestAction = ' ' #default to N
    else:
        correctDirProb = 1 - grid.noise
        slipProb = grid.noise /2
        discount = grid.discount

        for a in state.actions:
            value = 0
            if a == 'S': # probability, utility, 1-probability, utility
                if y-1 >= 0:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y-1].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x-1 >= 0:
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x+1 < grid.width:
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility ) # + DISCOUNTED UTILITY OF S'v
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
            if a == 'N':
                if y+1 < grid.height:
                    value += correctDirProb* (state.cost + discount * grid.grid[x][y+1].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x-1 >= 0:
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x+1 < grid.width:
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility )# + DISCOUNTED UTILITY OF S'v
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
            if a == 'E':
                if x+1 < grid.width:
                    value += correctDirProb * (state.cost + discount * grid.grid[x+1][y].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y+1 < grid.height:
                    value += slipProb * (state.cost + discount * grid.grid[x][y+1].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y-1 >= 0:
                    value += slipProb * (state.cost + discount *  grid.grid[x][y-1].utility )# + DISCOUNTED UTILITY OF S'v
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
            if a == 'W':
                if x-1 >= 0:
                    value += correctDirProb * (state.cost + discount * grid.grid[x-1][y].utility) 
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y+1 < grid.height:
                    value += slipProb * (state.cost + discount *  grid.grid[x][y+1].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y-1 >=0:
                    value += slipProb * (state.cost + discount * grid.grid[x][y-1].utility )# + DISCOUNTED UTILITY OF S'v
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
            
            if value > maxValue:
                maxValue = value
                bestAction = a
    

    return [maxValue, bestAction]


def main():
    grid = setupGrid()
    
    k = 5 #grid.K
    iteration = 0

    while iteration < k:
        maxValue = 0
        for x in range(grid.width):
            for y in range(grid.height):
                state = grid.grid[x][y]
                for a in state.actions:
                    [state.utility, state.policy] = bellman(state, grid, x, y)
        iteration += 1

    grid.printUtility();

    #    optimal policy = max of all values?
    #return optimal policy for all states in grid world



if __name__ == "__main__":
    main()
