import sys

class Results:
    
    X = 0
    Y = 1
    STEP = 2
    METHOD = 3
    QUERY = 4

    def __init__(self):
        self.queries = []
        self.results = []

        fileName = "results.txt"
        if len(sys.argv) > 1:
            fileName = sys.argv[2]

        print(f"Looking for queries in file {fileName}")
        try:
            filePath = fileName
            file = open(filePath)
        except FileNotFoundError:
            print(f"\033[0;31mCouldn't find file {fileName}.... Please try again.\033[0;37m")
            exit()
        
        Lines = file.readlines()
        for line in Lines:
            query = line.strip().split(',')
            self.queries.append(query)



    def checkResults(self, step, method, grid):
        for query in self.queries:
            if method == query[self.METHOD] :
                if int(step) == int(query[self.STEP]) :
                    #ANSWER THE QUERY
                    x = int(query[self.X])
                    y = int(query[self.Y])
                    if(x < grid.width and y < grid.height):
                        if(query[self.METHOD] == "MDP"):
                            if query[self.QUERY] == "stateValue":
                                value = grid.grid[x][y].stateValue()
                            else: # bestPolicy
                                value = grid.grid[x][y].bestPolicy()

                            result = str(query)[1:-1] + ": " +  str(value)
                            self.results.append(result)
                        elif(query[self.METHOD] == "RL"):
                            if query[self.QUERY] == "bestQValue":
                                value = grid.grid[x][y].bestQValue()
                            else: # bestPolicy
                                value = grid.grid[x][y].bestQPolicy()

                            result = str(query)[1:-1] + ": " +  str(value)
                            self.results.append(result)
                        else:
                            print("INVALID QUERY")


    
    #toString function
    def __str__(self):
        message = ""
        for result in self.results:
            message = message + result + '\n'
        return message
    
    #another toString function (idk its some python stuff)
    def __repr__(self):
        message = ""
        for result in self.results:
            message = message + result + '\n'
        return message