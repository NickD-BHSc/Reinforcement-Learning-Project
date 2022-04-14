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
    print(line)
    line = file.readline().split('=') # y=?
    y = int(line[1])
    line = file.readline().split('=') # Terminal=?
    terminalString = line[1]
    line = file.readline().split('=') # Boulder=?
    boulderString = line[1]
    line = file.readline().split('=') # RobotStartState=?
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

    grid = [[State(2)] * x] * y  ## create a grid of size x y filled with empty States

    #Set up terminals
    print (re.findall(r'(?<=\{)(.*?)(?=\})', terminalString))
    terminalString = terminalString.split('{')
    for s in terminalString:
        s = s.split('=')[1]
        s = s.replace('{', '')
        s = s.splot


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