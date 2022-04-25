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
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility ) # + DISCOUNTED UTILITY OF S'v
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
                    value += slipProb * (state.cost + discount * grid.grid[x+1][y].utility )# + DISCOUNTED UTILITY OF S'v
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
                    value += slipProb * (state.cost + discount *  grid.grid[x][y-1].utility )# + DISCOUNTED UTILITY OF S'v
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
                    value += slipProb * (state.cost + discount * grid.grid[x][y-1].utility )# + DISCOUNTED UTILITY OF S'v
                else:
                    value += slipProb * (state.cost + discount * grid.grid[x][y].utility) 

            if value > maxValue:
                maxValue = value
                bestAction = a
    

    return [maxValue, bestAction]