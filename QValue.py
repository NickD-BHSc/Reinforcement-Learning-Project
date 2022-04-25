
from sre_parse import State
import random

def getQValue(state, action):
    pass


def getValue( state):
    pass

#return max of all Qvalues
def getPolicy(state):
    maximum = 'N'
    for i in state.qvalues:
        i
    return max(state.qvalues.values() )

def update(state, action, nextState, reward):
    pass

# sooo, random for first few episodes. then getpolicy based on MAX qvalue. 
# then if theres negative values, it's worthwhile for agent to 'explore places it hasn't yet' 
# i.e. 0 value qvalue. so pick based on q values, then based on random if there are 0.0 ties
def qValueCalculation(currState, grid, direction):
    x = int(currState[0])
    y = int(currState[1])
    state = grid.grid[x][y]
    nextDir = None
    correctDirProb = 1 - grid.noise
    slipProb = grid.noise /2
    discount = grid.discount
    value = 0
    

    # South
    if direction == 'S': # probability, utility, 1-probability, utility
        nextDir = random.choices(['S', 'E', 'W'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
        if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
    elif direction == 'N': # probability, utility, 1-probability, utility
        nextDir = random.choices(['N', 'E', 'W'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
        if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
    elif direction == 'E': # probability, utility, 1-probability, utility
        nextDir = random.choices(['E', 'S', 'N'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if y+1 >= 0 and grid.grid[x][y+1].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x][y+1].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
        if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
    else: # direction == 'W': # probability, utility, 1-probability, utility
        nextDir = random.choices(['W', 'N', 'S'], weights=(correctDirProb, slipProb, slipProb) ) ## get next state
        if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
            value += correctDirProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
        else:
            value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
        if y+1 < grid.width and grid.grid[x][y+1].symbol != 'B':
            value += slipProb * (state.cost + discount * max(grid.grid[x][y+1].qvalues.values()) )
        else:
            value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )

    
    # print(f"max: {max(state.qvalues, key=state.qvalues.get)}")
    # bestPolicy = max(state.qvalues, key=state.qvalues.get)
    return [value, str(nextDir[0])]
    

def episode(grid):
    # North, South, East, West
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
            bestQValue, nextDir = qValueCalculation(stateLocation, grid, direction)
            #UPDATE the QVALUE
            #Average of the current and the new ( curr+new / 2 )
            if direction == 'N':
                currState.qvalues['N'] = (currState.qvalues['N'] + bestQValue)/2
            elif direction == 'S':
                currState.qvalues['S'] = (currState.qvalues['S'] + bestQValue)/2
            elif direction == 'E':
                currState.qvalues['E'] = (currState.qvalues['E'] + bestQValue)/2
            elif direction == 'W':
                currState.qvalues['W'] = (currState.qvalues['W'] + bestQValue)/2
            #Update the state
            if nextDir == 'N':
                stateLocation = [ stateLocation[0],  stateLocation[1] - 1]
                currState = grid.grid[ stateLocation[0]][ stateLocation[1]]
            elif nextDir == 'S':
                stateLocation = [ stateLocation[0],  stateLocation[1] + 1]
                currState = grid.grid[ stateLocation[0]][ stateLocation[1]]
            elif nextDir == 'E':
                stateLocation = [ stateLocation[0] + 1,  stateLocation[1]]
                currState = grid.grid[stateLocation[0]][stateLocation[1]]
            elif nextDir == 'W':
                stateLocation = [ stateLocation[0] - 1,  stateLocation[1]]
                currState = grid.grid[stateLocation[0]][stateLocation[1]]
            print(f"Going: {nextDir}")
            print(f"At state: {stateLocation}")
