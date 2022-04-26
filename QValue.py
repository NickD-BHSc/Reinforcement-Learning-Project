# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401
# Aim: Implement Value Iteration and Q-Value learning algorithms to train an agent to navigate a grid world

from sre_parse import State
import random

# IsValidLocation: checks if next location is valid. Takes in the grid, the direction, the x/y-coordinates.
# Returns whether or not the location is valid (not a boulder, not outside the grid)
def isValidLocation(grid, dir, x, y):
    if dir == 'N':
        return  y+1 < grid.height and grid.grid[x][y+1].symbol != 'B'
    elif dir == 'S':
        return y-1 >= 0 and grid.grid[x][y-1].symbol != 'B'
    elif dir == 'W':
        return x-1 >= 0 and grid.grid[x-1][y].symbol != 'B'
    elif dir == 'E':
        return x+1 < grid.width and grid.grid[x+1][y].symbol != 'B'
    

# getPolicy: computes the best action to take in a state. Takes in the state.
# Returns best action to take in state
def getPolicy(state):
    return max(state.qvalues, key=state.qvalues.get)

# update: performs q-value update for the state. Takes in state, location, grid, action, reward.
# Returns the next state and its location
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

# getQValue: computes q. Takes in the x/y-coordinates, state, discount, probability, grid.
# Returns q
def getQValue(x, y, state, discount, probability, grid):
    return probability * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )

# getValue: computes the max action q over legal actions. Takes in the current state, grid, direction to look.
# returns max action Q over legal actions and the direction
def getValue(currState, grid, direction):
    x = int(currState[0])
    y = int(currState[1])
    state = grid.grid[x][y]
    nextDir = None
    correctDirProb = 1 - grid.noise
    slipProb = grid.noise /2
    discount = grid.discount
    value = 0
    
    if direction == 'N':
        nextDir = random.choices(['N', 'E', 'W'], weights=(correctDirProb, slipProb, slipProb) )
        if y+1 < grid.height and grid.grid[x][y+1].symbol != 'B':
            value = getQValue(x, y+1, state, discount, correctDirProb, grid)
        else:
            value = getQValue(x, y, state, discount, correctDirProb, grid)
    elif direction == 'S':
        nextDir = random.choices(['S', 'E', 'W'], weights=(correctDirProb, slipProb, slipProb) )
        if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
            value = getQValue(x, y-1, state, discount, correctDirProb, grid)
        else:
            value = getQValue(x, y, state, discount, correctDirProb, grid)
    elif direction == 'E':
        nextDir = random.choices(['E', 'S', 'N'], weights=(correctDirProb, slipProb, slipProb) )
        if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
            value = getQValue(x+1, y, state, discount, correctDirProb, grid)
        else:
            value = getQValue(x, y, state, discount, correctDirProb, grid)
    else:
        nextDir = random.choices(['W', 'N', 'S'], weights=(correctDirProb, slipProb, slipProb) )
        if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
            value = getQValue(x-1, y, state, discount, correctDirProb, grid)
        else:
            value = getQValue(x, y, state, discount, correctDirProb, grid)

    return [value, str(nextDir[0])]
    
# getNextDir: chooses the next direction for the agent to go. Takes in grid, state.
# Returns the next direction for the agent to go.
def getNextDir(grid, state):
    sort = sorted(state.qvalues.items(), key=lambda x: x[1])
    alpha = grid.alpha
    rand = (1-alpha)/3
    choice = random.choices(sort, weights=(rand, rand, rand, alpha) )[0]
    return choice[0]

# episode: Run an episode of RL algorithm until we exit from a terminal state. Takes in the grid.
def episode(grid):
    currState = grid.grid[int(grid.startState[0])][int(grid.startState[1])]
    stateLocation = [int(grid.startState[0]), int(grid.startState[1]) ]
    done = False
    while not done:
        if currState.symbol == 'T':
            currState.qvalues['EXIT'] = (currState.qvalues['EXIT'] + currState.cost) /2
            done = True
        else:
            direction = getNextDir(grid, currState)
            bestQValue, nextDir = getValue(stateLocation, grid, direction)
            currState, stateLocation = update(currState, stateLocation, grid, nextDir, bestQValue)
            
