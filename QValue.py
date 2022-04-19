
from sre_parse import State
import random

def qValueCalculation(state, grid, x, y):
    maxValue = 0
    bestAction = 'N' #default to N
    if state.symbol == 'T':
        maxValue = state.cost
        bestAction = ' '
    else:
        correctDirProb = 1 - grid.noise
        slipProb = grid.noise /2
        discount = grid.discount

        for a in state.actions:
            value = 0
            # South
            if y == 1: # probability, utility, 1-probability, utility
                if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                    value += correctDirProb * (state.cost + discount * max(state.qvalues.values()) )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility ) # + DISCOUNTED UTILITY OF S'v
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility)


    maxQValue = max(allQValues)
    [grid.grid[x][y-1].utility, grid.grid[x][y-1].utility, grid.grid[x][y-1].utility, grid.grid[x][y-1].utility]

def episode(grid):
    # North, South, East, West
    directions = [[0,-1],[0,1],[1,0],[-1,0]]

    state = grid.startState
    done = False
    while not done:
        direction = random.choice(directions)
        direction = directions.index(nextState)
        qValueCurr = qValueCalculation(state, grid, nextState[0], nextState[1])
        
        if direction == 0:
            state.qvalues['N'] = qValueCurr
        if direction == 1:
            direction = 'S'
        if direction == 2:
            direction = 'E'
        if direction == 3:
            direction = 'W'

        
        
        check if we're done



"""
    if state.symbol == 'T':
        maxValue = state.cost
        bestAction = ' '
    else:
        correctDirProb = 1 - grid.noise
        slipProb = grid.noise /2
        discount = grid.discount

        for a in state.actions:
            value = 0
            if a == 'S': # probability, utility, 1-probability, utility
                if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y-1].utility )
                else:"""