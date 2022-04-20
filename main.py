import sys
from states import State, Boulder, Terminal
from grid import Grid, setupGrid
from ValueIteration import bellman
import random

def updateResults(k):
    pass

def main():
    grid = setupGrid()
    
    if False:
        k = 1 #grid.K
        iteration = 0

        while iteration < k:
            for x in range(grid.width):
                for y in range(grid.height):
                    state = grid.grid[x][y]
                    for a in state.actions:
                        [state.utility, state.policy] = bellman(state, grid, x, y)
            updateResults(k)
            iteration += 1

        grid.printUtility()
    
    grid.printQvalue()
directions = [[0,-1],[0,1],[1,0],[-1,0]]


if __name__ == "__main__":
    main()
    x = random.choice(directions)
    print(f"state: {x}, x:{x[0]}, y:{x[1]}")
