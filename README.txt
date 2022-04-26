# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401
# Aim: Implement Value Iteration and Q-Value learning algorithms to train an agent to navigate a grid world

A total of 6 files should be present and is required to run this program.
1) grid.py
2) main.py
3) QValue.py
4) states.py
5) ValueIteration.py
6) results.py

A 7th file detailing the grid configuration and 8th file detailing the queries, are also required (in command line) to pass into the program.
7) gridConf.txt
8) results.txt

# To Run:
In root directory, please Run
`python main.py <gridConf.txt> <results.txt>`

<gridConf.txt> - the grid configuration file name that you want to run (including extension)
<results.txt> - the results file name that you want to run (including extension)


We programmed our own graphical representation (extraneous to provided gui and instructions for this assignment), to provide convenience in showing ValueIteration and Q-Value Learning values. Formatting was tested for values up to 3 significant figures (additional significant figures might result in slightly warped graphical representation).

## Value Iteration values:
Are provided with [optimalValue : optimalDirection] pairing, (ex. `0.8:N`). Directions are `N: North`, `E: East`, `S: South`, `W: West`
Cells with boulders do not have a [optimalValue : optimalDirection] pair, rather they are depicted with `B: ,`. Terminal states also do not have a [optimalValue : optimalDirection] pair, rather they are depicted with just their terminal value (defined in the grid configuration file) (ex. `1: ,`).

## Q-Value Learning values:
Are provided with 4 directions and their respective optimal values

example:
                `0.7` (for North)
(for West) `0.4`     `0.5` (for East)
                `0.2` (for South)

Terminals only output terminal value; Boulders output a block of #


# Note:
The contents in the gridConf.txt MUST follow the layout provided in the assignment instruction details:

x=4

y=3

Terminal={1={3,1,-1},2={3,2,1}}           // if no terminal states, please provide empty set Terminal={}

Boulder={1={1,1}}                         // if no boulder states, please provide empty set Boulder={}

RobotStartState={0,0}                     // if no robotstart state, please provide empty set RobotStartState={}

K=1000

Episodes=3500

alpha=0.2

Discount=0.9

Noise=0.2

TransitionCost=0

