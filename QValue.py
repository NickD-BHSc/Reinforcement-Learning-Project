# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401

from sre_parse import State
import random


# TODOS:
# getvalue function
# results parsing and output
# print grid graphical for qvalue in this version is behind

def getValue( state):
    pass

def isValidLocation(grid, dir, x, y):
    if dir == 'N':
        return  y+1 < grid.height and grid.grid[x][y+1].symbol != 'B'
    elif dir == 'S':
        return y-1 >= 0 and grid.grid[x][y-1].symbol != 'B'
    elif dir == 'W':
        return x-1 >= 0 and grid.grid[x-1][y].symbol != 'B'
    elif dir == 'E':
        return x+1 < grid.width and grid.grid[x+1][y].symbol != 'B'
    

#return max of all Qvalues
def getPolicy(state):
    return max(state.qvalues, key=state.qvalues.get)

def update(state, location, grid, action, reward):
    if action == 'N':
        state.qvalues['N'] = (state.qvalues['N'] + reward)/2
    elif action == 'S':
        state.qvalues['S'] = (state.qvalues['S'] + reward)/2
    elif action == 'E':
        state.qvalues['E'] = (state.qvalues['E'] + reward)/2
    elif action == 'W':
        state.qvalues['W'] = (state.qvalues['W'] + reward)/2
    #Update the state
    if action == 'S':
        nextLocation = [ location[0],  location[1] - 1]
    elif action == 'N':
        nextLocation = [ location[0],  location[1] + 1]
    elif action == 'E':
        nextLocation = [ location[0] + 1,  location[1]]
    elif action == 'W':
        nextLocation = [ location[0] - 1,  location[1]]
    
    if not isValidLocation(grid, action, location[0], location[1]):
        nextState = state
        nextLocation = location
    else:
        nextState = grid.grid[nextLocation[0]][nextLocation[1]]
    return nextState, nextLocation

def getQValue(currState, grid, direction):
    x = int(currState[0])
    y = int(currState[1])
    state = grid.grid[x][y]
    nextDir = None
    correctDirProb = 1 - grid.noise
    slipProb = grid.noise /2
    discount = grid.discount
    value = 0
    

    # South
    if direction == 'N': # probability, utility, 1-probability, utility
        nextDir = random.choices(['N', 'E', 'W'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if y+1 < grid.height and grid.grid[x][y+1].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y+1].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
    elif direction == 'S': # probability, utility, 1-probability, utility
        nextDir = random.choices(['S', 'E', 'W'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
    elif direction == 'E': # probability, utility, 1-probability, utility
        nextDir = random.choices(['E', 'S', 'N'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
    else: # direction == 'W': # probability, utility, 1-probability, utility
        nextDir = random.choices(['W', 'N', 'S'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )

    return [value, str(nextDir[0])]
    

def episode(grid):
    # North, East, South, West
    directions = ['N','E','S','W']

    currState = grid.grid[int(grid.startState[0])][int(grid.startState[1])]
    stateLocation = [int(grid.startState[0]), int(grid.startState[1]) ]
    done = False
    while not done:
        
        if currState.symbol == 'T':
            currState.qvalues['EXIT'] = (currState.qvalues['EXIT'] + currState.cost) /2
            done = True
        else:
            direction = random.choice(directions)
            bestQValue, nextDir = getQValue(stateLocation, grid, direction)
            #UPDATE the QVALUE
            #Average of the current and the new ( curr+new / 2 )
            currState, stateLocation = update(currState, stateLocation, grid, nextDir, bestQValue)
            
