import sys
import re
from states import State, Boulder, Terminal, Robot

class Grid():

    def __init__(self, grid):
        self.grid = grid    
        
    #toString function
    def __str__(self):
        result = ''
        for i in range(3):
            result += '['
            for j in range(4):
                result += str(self.grid[j][i]) + ' '
            result += ']\n'

        return result
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        return "Grid"

def checkTerminals(agentPosition, terminalPositions):
    for tPosition in terminalPositions:
        if agentPosition[0] == tPosition[0] and agentPosition[1] == tPosition[1]:
            return True
    return False


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
    robotStartString = line
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

    grid = [ [State(transitionCost)]*y for i in range(x)]  ## create a grid of size x y filled with empty States

    #Set up terminals
    terminalString = terminalString[10:]
    terminalString = re.findall(r'(?<=\{)(.*?)(?=\})', terminalString)

    terminalPos = []
    
    for s in terminalString:
        s = s.split(',')
        coords = []
        xPos = int(s[0])
        yPos = int(s[1])
        coords.append(xPos)
        coords.append(yPos)
        cost = int(s[2])
        grid[xPos][yPos] = Terminal(cost)
        terminalPos.append(coords)

    print(f"tP: {terminalPos}")
    #Set up boulders
    boulderString = boulderString[9:]
    print(boulderString)
    boulderString = re.findall(r'(?<=\{)(.*?)(?=\})', boulderString)
    
    for s in boulderString:
        s = s.split(',')
        xPos = int(s[0])
        yPos = int(s[1])
        grid[xPos][yPos] = Boulder()

    robotStartString = robotStartString[16:]
    robotStartString = re.findall(r'(?<=\{)(.*?)(?=\})', robotStartString)
    
    agentPos = []
    for s in robotStartString:
        s = s.split(',')
        xPos = int(s[0])
        agentPos.append(xPos)
        yPos = int(s[1])
        agentPos.append(yPos)
        grid[xPos][yPos] = Robot()
        # print(f"x:{xPos},y:{yPos}")

    #Terminal = Terminal(line[1])

    # this check works
    while not checkTerminals(agentPos, terminalPos):
        # make a random choice of which direction to go
        # ex go north
        # compute the value:
        # v(k+1) = (probability1 * transition * (reward + discount*prevState)) + (probability2 * transition * (reward + discount*prevState))
        nextStep = probability * currValue * (reward + discount * prevState) + 1-probability * 
        # agentPos[0] = 3
        # agentPos[1] = 1
        # print(f"cek")

    print(f"robot: {agentPos[1]}")
    #finished parsing, try to solve
    #solve(problem)

    # while agentPos != 


    print(f"tc: {transitionCost}")
    
    # while 

    file.close()
    return grid