import sys
import re
from states import State, Boulder, Terminal

class Grid():

    def __init__(self, grid, width, height, K, discount, noise):
        self.grid = grid
        self.width = width
        self.height = height     
        self.K = K
        self.noise = noise
        self.discount = discount

        
    def checkTerminals(self, agentPosition):
        if self.grid[agentPosition[0]][agentPosition[1]].symbol == 'T':
            return True
        return False
    
    def getGrid(self):
        return self.grid

    def printUtility(self):
        result = ''
        for i in range(self.height):
            result += '['
            for j in range(self.width):
                state = self.grid[j][self.height-1 - i]
                if state.symbol == 'B':
                    result += 'B: , '
                else:
                    result += str(round(state.utility, 2)) + ':'+ state.policy + ', '
            result += ']\n'
        print(result)

    #toString function
    def __str__(self):
        result = ''
        for i in range(self.height):
            result += '['
            for j in range(self.width):
                result += str(self.grid[j][self.height-1 - i]) + ' '
            result += ']\n'

        return result
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        return "Grid"



#sets up the grid from a file
def setupGrid():
    fileName = "gridFiles/gridConf.txt"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]

    print(f"Solving puzzles in file: {fileName}")
    try:
        file = open(fileName)
    except FileNotFoundError:
        print("Couldn't find file {filename}.... Please try again.")
        exit()


    ## START PARSING
    line = file.readline().split('=') # x=?
    x = int(line[1])
    line = file.readline().split('=') # y=?
    y = int(line[1])
    line = file.readline() # Terminal=?
    terminalString = line
    line = file.readline() # Boulder=?
    boulderString = line
    line = file.readline() # RobotStartState=?
    robotStartString = line[1]
    line = file.readline().split('=') # K=?
    K = int(line[1])
    line = file.readline().split('=') # Episodes=?
    Episodes = int(line[1])
    line = file.readline().split('=') # Alpha=?
    alpha = float(line[1])
    line = file.readline().split('=') # discount=?
    discount = float(line[1])
    line = file.readline().split('=') # noise=?
    noise = float(line[1])
    line = file.readline().split('=') # transitionCost=?
    transitionCost = float(line[1])

    grid = [ [0]*y for i in range(x)]  ## create a grid of size x y filled with empty States

    for i in range(x):
        for j in range(y):
            grid[i][j] = State(transitionCost)

    #Set up terminals
    terminalString = terminalString[10:]
    terminalString = re.findall(r'(?<=\{)(.*?)(?=\})', terminalString)

    
    for s in terminalString:
        s = s.split(',')
        xPos = int(s[0])
        yPos = int(s[1])
        cost = int(s[2])
        grid[xPos][yPos] = Terminal(cost)

    #Set up boulders
    boulderString = boulderString[9:]
    boulderString = re.findall(r'(?<=\{)(.*?)(?=\})', boulderString)
    
    for s in boulderString:
        s = s.split(',')
        xPos = int(s[0])
        yPos = int(s[1])
        grid[xPos][yPos] = Boulder()

    #Terminal = Terminal(line[1])

    #finished parsing, try to solve
    #solve(problem)

    file.close()
    
    return Grid(grid, x, y, K, discount, noise)