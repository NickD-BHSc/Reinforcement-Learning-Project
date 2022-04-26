# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401
# Aim: Implement Value Iteration and Q-Value learning algorithms to train an agent to navigate a grid world

import sys
from states import State, Boulder, Terminal
from grid import Grid, setupGrid
from ValueIteration import bellman
from QValue import episode
from results import Results

# start of program
def main():
    print("#####################################\n")
    grid = setupGrid()
    results = Results()
    
    print(f"Robot starting at: {grid.startState}\n")

    #Value Iteration
    k = grid.K
    iteration = 0
    print("Running Value Iteration...")
    print(f"{k} iterations to run")
    while iteration < k:
        for x in range(grid.width):
            for y in range(grid.height):
                state = grid.grid[x][y]
                for a in state.actions:
                    [state.utility, state.policy] = bellman(state, grid, x, y)
        results.checkResults(iteration, "MDP", grid)
        iteration += 1
    print(f"Graphical Representation after ALL iterations:")
    grid.printUtility()

    #QValue Learning
    maxEpisodes = grid.Episodes
    episodes = 0
    print("Running Q-Value Learning...")
    print(f"{maxEpisodes} episodes to run")
    while episodes < maxEpisodes:
        episode(grid)
        results.checkResults(episodes, "RL", grid)
        episodes += 1
    print(f"Graphical Representation after ALL episodes:")
    grid.printQvalue()

    print("\n\033[96mRESULTS:\033[0;37m")
    print(results)
    
directions = [[0,-1],[0,1],[1,0],[-1,0]]


if __name__ == "__main__":
    main()
