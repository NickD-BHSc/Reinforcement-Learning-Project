# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401

import sys
from states import State, Boulder, Terminal
from grid import Grid, setupGrid
from ValueIteration import bellman
from QValue import episode

def updateResults(k):
    pass

# def qValueLearning():


def main():
    grid = setupGrid()
    
    
    print(f"Robot starting at: {grid.startState}")

    maxEpisodes = grid.Episodes
    episodes = 0
    print("Running QValue Learning...")
    while episodes < maxEpisodes:
        episode(grid)
        episodes += 1

    grid.printQvalue()
    

    k = grid.K
    iteration = 0
    print("Running Value Iteration...")
    #VALUE ITERATION
    while iteration < k:
        for x in range(grid.width):
            for y in range(grid.height):
                state = grid.grid[x][y]
                for a in state.actions:
                    [state.utility, state.policy] = bellman(state, grid, x, y)
        updateResults(k)
        iteration += 1

    grid.printUtility()
    
directions = [[0,-1],[0,1],[1,0],[-1,0]]


if __name__ == "__main__":
    main()
    
    # print(f"state: {x}, x:{x[0]}, y:{x[1]}")
    
