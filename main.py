import sys
from turtle import right
from states import State, Boulder, Terminal
from grid import Grid, setupGrid


def bellman(state, grid, x, y):
    
    maxValue = 0
    if state.symbol == 'T':
        maxValue = state.cost
    else:
        correctDirProb = 1 - grid.noise
        slipProb = grid.noise /2
        discount = grid.discount

        bestAction = 'N' #
        for a in state.actions:
            value = 0
            if a == 'N': # probability, utility, 1-probability, utility
                if y-1 >= 0 and grid.grid[x][y-1].symbol == 'B':
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y-1].utility )
                if x-1 >= 0:
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                if x+1 < grid.width:
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility ) # + DISCOUNTED UTILITY OF S'v
            if a == 'S':
                if y+1 < grid.height:
                    value += correctDirProb* (state.cost + discount * grid.grid[x][y+1].utility )
                if x-1 >= 0:
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                if x+1 < grid.width:
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility )# + DISCOUNTED UTILITY OF S'v
            if a == 'E':
                if x+1 < grid.width:
                    value += correctDirProb * (state.cost + discount * grid.grid[x+1][y].utility )
                if y+1 < grid.height:
                    value += slipProb * (state.cost + discount * grid.grid[x][y+1].utility )
                if y-1 >= 0:
                    value += slipProb * (state.cost + discount *  grid.grid[x][y-1].utility )# + DISCOUNTED UTILITY OF S'v
            if a == 'W':
                if x-1 >= 0:
                    value += correctDirProb * (state.cost + discount * grid.grid[x-1][y].utility) 
                if y+1 < grid.height:
                    value += slipProb * (state.cost + discount *  grid.grid[x][y+1].utility )
                if y-1 >=0:
                    value += slipProb * (state.cost + discount * grid.grid[x][y-1].utility )# + DISCOUNTED UTILITY OF S'v
            
            if value > maxValue:
                maxValue = value
                bestAction = a
    

    return maxValue


def main():
    grid = setupGrid()
    
    k = 2 #grid.K
    iteration = 0

    while iteration < k:
        for x in range(grid.width):
            for y in range(grid.height):
                state = grid.grid[x][y]
                for a in state.actions:
                    state.utility = bellman(state, grid, x, y)
        iteration += 1

    grid.printUtility()

    #    optimal policy = max of all values?
    #return optimal policy for all states in grid world



if __name__ == "__main__":
    main()
