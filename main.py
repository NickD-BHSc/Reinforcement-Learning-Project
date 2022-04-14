import sys
from states import State, Boulder, Terminal
from grid import Grid, setupGrid

def main():
    grid = setupGrid()
    grid = Grid(grid)
    
    print(grid)


if __name__ == "__main__":
    main()
