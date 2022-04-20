
from sre_parse import State
import random
class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discount (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)

    "*** YOUR CODE HERE ***"

  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def qValueCalculation(currState, grid, direction):
    x = int(currState[0])
    y = int(currState[1])
    state = grid.grid[x][y]
    if state.symbol == 'T':
        value = state.cost
        return [value, 'T']
    else:
        correctDirProb = 1 - grid.noise
        slipProb = grid.noise /2
        discount = grid.discount
        value = 0

        # South
        if direction == 'S': # probability, utility, 1-probability, utility
            if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
            else:
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
            if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
            if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if direction == 'N': # probability, utility, 1-probability, utility
            if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
            else:
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
            if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
            if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if direction == 'E': # probability, utility, 1-probability, utility
            if x+1 < grid.width and grid.grid[x+1][y].symbol != 'B':
                value += correctDirProb * (state.cost + discount * max(grid.grid[x+1][y].qvalues.values()) )
            else:
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
            if y+1 >= 0 and grid.grid[x][y+1].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x][y+1].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
            if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
            else:
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
        if direction == 'W': # probability, utility, 1-probability, utility
            if x-1 >= 0 and grid.grid[x-1][y].symbol != 'B':
                value += correctDirProb * (state.cost + discount * max(grid.grid[x-1][y].qvalues.values()) )
            else:
                value += correctDirProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )
            if y-1 >= 0 and grid.grid[x][y-1].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x][y-1].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) ) 
            if y+1 < grid.width and grid.grid[x][y+1].symbol != 'B':
                value += slipProb * (state.cost + discount * max(grid.grid[x][y+1].qvalues.values()) )
            else:
                value += slipProb * (state.cost + discount * max(grid.grid[x][y].qvalues.values()) )

    
    # print(f"max: {max(state.qvalues, key=state.qvalues.get)}")
    # bestPolicy = max(state.qvalues, key=state.qvalues.get)
    return [value, '_']
    

def episode(grid):
    # North, South, East, West
    directions = ['N','E','S','W']

    currState = grid.startState
    nextState = currState
    done = False
    while not done:
        direction = random.choice(directions)
        bestQValue, stateSymbol = qValueCalculation(currState, grid, direction)
        
        x = int(currState[0])
        y = int(currState[1])
        currState = grid.grid[x][y]

        # need it to actually give back which direction it went in order to proceed with learning
        
        if direction == 'N':
            currState.qvalues['N'] = bestQValue
            currState = [x,y-1]
        elif direction == 'S':
            currState.qvalues['S'] = bestQValue
        elif direction == 'E':
            currState.qvalues['E'] = bestQValue
        elif direction == 'W':
            currState.qvalues['W'] = bestQValue
        

        if stateSymbol == 'T':
            done = True
        else:
            print(f"currrrrState: {currState}")
            currState = [x,y] # plus whichever direction its supposed to go
