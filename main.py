import sys
import re
from states import State, Boulder, Terminal

def parseFile():    
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

    grid = [ [State(transitionCost)]*y for i in range(x)]  ## create a grid of size x y filled with empty States

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
    print(boulderString)
    boulderString = re.findall(r'(?<=\{)(.*?)(?=\})', boulderString)
    
    for s in boulderString:
        s = s.split(',')
        xPos = int(s[0])
        yPos = int(s[1])
        grid[xPos][yPos] = Boulder()
        print(s)

    print("heres the grid")
    print(grid)

    #Terminal = Terminal(line[1])

    #finished parsing, try to solve
    #solve(problem)

    file.close()

def main():
    parseFile()

if __name__ == "__main__":
    main()
