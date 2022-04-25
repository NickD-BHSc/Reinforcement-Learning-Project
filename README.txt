# COMP 4190: A3 - Reinforcement Learning
# Instructor: Dr. Cuneyt G Akcora
# Student Names and Numbers:
# Aaron Salo - 7805174
# Nicholas Duan - 7742401

A total of 5 files should be present and is required to run this program.
1) grid.py
2) main.py
3) QValue.py
4) states.py
5) ValueIteration.py
A 6th file detailing the grid configuration is also required to pass into the RL algorithm.
6) gridfile.txt

# To Run:
In root directory, please Run
`python main.py <gridfilename>`

<gridfilename> - the grid file name that you want to run (without the '.txt' extension)


We programmed our own graphical representation (extraneous to provided gui and instructions for this assignment), to provide convenience in showing ValueIteration and Q-Value Learning values. Formatting was tested for values up to 3 decimal places (additional significant figures might result in slightly warped figure).

Value Iteration values are provided with [optimal value:optimal direction] pairing, (ex. 0.8:N).
Q-Value Learning values are provided with 4 directions and their respective optimal value

example:
                 0.7 `(for North)`
`(for West)` 0.4     0.5 `(for East)`
                 0.2 `(for South)`


