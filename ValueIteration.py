# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401
# Aim: Implement Value Iteration and Q-Value learning algorithms to train an agent to navigate a grid world

# Bellman equation for value iteration. Takes in the state, the grid, the x/y-coordinates.
# Returns the max value and its action for the state
def bellman(state, grid, x, y):
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
            if a == 'S': # probability, utility, 1-probability, utility
                if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y-1].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
            if a == 'N':
                if y+1 < grid.height and grid.grid[x][y+1].symbol != 'B':
                    value += correctDirProb* (state.cost + discount * grid.grid[x][y+1].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x-1][y].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
                if x+1 < grid.width:
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
            if a == 'E':
                if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
                    value += correctDirProb * (state.cost + discount * grid.grid[x+1][y].utility )
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y+1 < grid.height and grid.grid[x][y+1].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x][y+1].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                    value += slipProb * (state.cost + discount *  grid.grid[x][y-1].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
            if a == 'W':
                if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                    value += correctDirProb * (state.cost + discount * grid.grid[x-1][y].utility) 
                else:
                    value += correctDirProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y+1 < grid.height and grid.grid[x][y+1].symbol != 'B':
                    value += slipProb * (state.cost + discount *  grid.grid[x][y+1].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 
                if y-1 >=0 and grid.grid[x][y-1].symbol != 'B':
                    value += slipProb * (state.cost + discount * grid.grid[x][y-1].utility )
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 

            if value > maxValue:
                maxValue = value
                bestAction = a
    
    return [maxValue, bestAction]