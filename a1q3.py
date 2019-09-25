#!/usr/bin/python
#CONSTANTS

NUM_COLS = 4
NUM_ROWS = 3
NUM_ACTIONS = 4
VALID_STATES = 9
COL = 0
ROW = 1
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
#Observation Models P(e | state)
#obs 1 wall
OBS_1WL = [[0.1, 0.1, 0.9, 0.1],[0.1, 0.0, 0.9, 0.0],[0.1, 0.1, 0.9, 0.0]]
#obs 2 wall
OBS_2WL = [[0.9, 0.9, 0.1, 0.9],[0.9, 0.0, 0.1, 0.0],[0.9, 0.9, 0.1, 0.0]]
#obs end
OBS_END = [[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 1.0],[0.0, 0.0, 0.0, 1.0]]
OBS_MODEL = [OBS_END, OBS_1WL, OBS_2WL]


#source for initializing a multi dimensional matrix in python https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
TRANSFORMATION = []
w  = NUM_ROWS+1
h = NUM_COLS+1
d = NUM_ACTIONS+1;
base = [[[0,0], 0.0], [[0,0], 0.0], [[0,0], 0.0], [[0,0], 0.0]]
TRANSFORMATION = [[[ base for x in range(w)] for y in range(h)] for z in range(d)]


# let current state be defined by [col][row]
# TRANSFORMATION[col][row][action]
#       = [prevState, p(currentState | action, prevState)]
TRANSFORMATION[1][1][UP] = [[[1,2], 0.0], [[1,1], 0.1], [[2,1], 0.1]]
TRANSFORMATION[1][1][DOWN] = [[[1,2], 0.8], [[1,1], 0.9], [[2,1], 0.1]]
TRANSFORMATION[1][1][LEFT] = [[[1,2], 0.1], [[1,1], 0.9], [[2,1], 0.8]]
TRANSFORMATION[1][1][RIGHT] = [[[1,2], 0.1], [[1,1], 0.1], [[2,1], 0.0]]

TRANSFORMATION[1][2][UP] = [[[1,1], 0.8], [[1,2], 0.2], [[1,3], 0.0]]
TRANSFORMATION[1][2][DOWN] = [[[1,1], 0.0], [[1,2], 0.2], [[1,3], 0.8]]
TRANSFORMATION[1][2][LEFT] = [[[1,1], 0.1], [[1,2], 0.8], [[1,3], 0.1]]
TRANSFORMATION[1][2][RIGHT] = [[[1,1], 0.1], [[1,2], 0.8], [[1,3], 0.1]]

TRANSFORMATION[1][3][UP] = [[[1,2], 0.8], [[1,3], 0.9], [[2,3], 0.1]]
TRANSFORMATION[1][3][DOWN] = [[[1,2], 0.0], [[1,3], 0.1], [[2,3], 0.1]]
TRANSFORMATION[1][3][LEFT] = [[[1,2], 0.1], [[1,3], 0.9], [[2,3], 0.8]]
TRANSFORMATION[1][3][RIGHT] = [[[1,2], 0.1], [[1,3], 0.1], [[2,3], 0.0]]

TRANSFORMATION[2][1][UP] = [[[1,1], 0.1], [[2,1], 0.8], [[3,1], 0.1]]
TRANSFORMATION[2][1][DOWN] = [[[1,1], 0.1], [[2,1], 0.8], [[3,1], 0.1]]
TRANSFORMATION[2][1][LEFT] = [[[1,1], 0.0], [[2,1], 0.2], [[3,1], 0.8]]
TRANSFORMATION[2][1][RIGHT] = [[[1,1], 0.8], [[2,1], 0.2], [[3,1], 0.0]]

TRANSFORMATION[2][3][UP] = [[[1,3], 0.1], [[2,3], 0.8], [[3,3], 0.1]]
TRANSFORMATION[2][3][DOWN] = [[[1,3], 0.1], [[2,3], 0.8], [[3,3], 0.1]]
TRANSFORMATION[2][3][LEFT] = [[[1,3], 0.0], [[2,3], 0.2], [[3,3], 0.8]]
TRANSFORMATION[2][3][RIGHT] = [[[1,3], 0.8], [[2,3], 0.2], [[3,3], 0.0]]

TRANSFORMATION[3][1][UP] = [[[2,1], 0.1], [[3,1], 0.0], [[3,2], 0.0], [[4,1], 0.1]]
TRANSFORMATION[3][1][DOWN] = [[[2,1], 0.1], [[3,1], 0.8], [[3,2], 0.8], [[4,1], 0.1]]
TRANSFORMATION[3][1][LEFT] = [[[2,1], 0.0], [[3,1], 0.1], [[3,2], 0.1], [[4,1], 0.8]]
TRANSFORMATION[3][1][RIGHT] = [[[2,1], 0.8], [[3,1], 0.1], [[3,2], 0.1], [[4,1], 0.0]]

TRANSFORMATION[3][2][UP] = [[[3,1], 0.8], [[3,2], 0.1], [[3,3], 0.0]]
TRANSFORMATION[3][2][DOWN] = [[[3,1], 0.0], [[3,2], 0.1], [[3,3], 0.8]]
TRANSFORMATION[3][2][LEFT] = [[[3,1], 0.1], [[3,2], 0.8], [[3,3], 0.1]]
TRANSFORMATION[3][2][RIGHT] = [[[3,1], 0.1], [[3,2], 0.0], [[3,3], 0.1]]

TRANSFORMATION[3][3][UP] = [[[2,3], 0.1], [[3,3], 0.8], [[3,2], 0.8]]
TRANSFORMATION[3][3][DOWN] = [[[2,3], 0.1], [[3,3], 0.0], [[3,2], 0.0]]
TRANSFORMATION[3][3][LEFT] = [[[2,3], 0.0], [[3,3], 0.1], [[3,2], 0.1]]
TRANSFORMATION[3][3][RIGHT] = [[[2,3], 0.8], [[3,3], 0.1], [[3,2], 0.1]]

TRANSFORMATION[4][1][UP] = [[[3,1], 0.1], [[4,1], 0.1]]
TRANSFORMATION[4][1][DOWN] = [[[3,1], 0.1], [[4,1], 0.9]]
TRANSFORMATION[4][1][LEFT] = [[[3,1], 0.0], [[4,1], 0.1]]
TRANSFORMATION[4][1][RIGHT] = [[[3,1], 0.8], [[4,1], 0.9]]

TRANSFORMATION[4][2][UP] = [[[3,2], 0.1], [[4,1], 0.8]]
TRANSFORMATION[4][2][DOWN] = [[3,2], 0.1], [[4,1], 0.0]
TRANSFORMATION[4][2][LEFT] = [[3,2], 0.0], [[4,1], 0.1]
TRANSFORMATION[4][2][RIGHT] = [[[3,2], 0.8], [[4,1], 0.1]]

TRANSFORMATION[4][3][UP] =[[[3,3], 0.1]]
TRANSFORMATION[4][3][DOWN] = [[[3,3], 0.1]]
TRANSFORMATION[4][3][LEFT] = [[[3,3], 0.0]]
TRANSFORMATION[4][3][RIGHT] = [[[3,3], 0.8]]



# inputs:
# a: sequence of actions
# e: sequence of observations
# b: belief state [col, row], default unknown
def pomdp(a, o, b = [0, 0] ):
    beliefStateDistribution = initBeliefs(b)
    for i in range(0,len(a)):
        beliefStateDistribution = updateBeliefs(a[i], o[i], beliefStateDistribution)
    return beliefStateDistribution

#inputs:
#a: single action
#o: single observation
#b: current belief state distirbution
#returns an update belief state distribution given the inputs
def updateBeliefs(a, o, b):
    evidence = getEvidenceValue(o)
    if (o == "end"):
        evidence = 0
    aIndex = getActionIndex(a)
    newBeliefState = [[0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0]]
    for col in range(0,NUM_COLS):
      for row in range(0,NUM_ROWS):
          print("new state: " + str(col + 1) + ", " + str(row + 1))
          print("action: " + a)
          print(TRANSFORMATION[col+1][row+1][aIndex])
          probOfNewState = sumProbNewStateGivenAction(a, TRANSFORMATION[col+1][row+1][aIndex], b)
          probEvidenceGivenNewState = OBS_MODEL[evidence][row][col]
          print("newBeliefState = " + str(probEvidenceGivenNewState) + " * " + str(probOfNewState))
          newBeliefState[row][col] = round(probEvidenceGivenNewState*probOfNewState, 3)
    return newBeliefState


def sumProbNewStateGivenAction(a, probPrevStates, prevStateBeliefs):
    sum = 0
    for x in probPrevStates:
        prevCol = x[0][0]
        prevRow = x[0][1]
        probCurrentGivenPrev = x[1]
        prevBelief = 0
        if (prevRow - 1 >= 0 and prevCol >= 0):
            prevBelief = prevStateBeliefs[prevRow-1][prevCol-1]
        print("sum += " + str(prevBelief) + " * " + str(probCurrentGivenPrev))
        sum += prevBelief*probCurrentGivenPrev
    return sum

#checks for "end case and returns 0" otherwise returns the observation unchanged.
def getEvidenceValue(observation):
    if (observation == "end"):
        return 0
    else:
        return observation

#converts an action as a string to it's integer value as defined in constants
def getActionIndex(a):
    if (a == "up"):
        return UP
    if (a == "down"):
        return DOWN
    if (a == "left"):
        return LEFT
    if (a == "right"):
        return RIGHT
    return -1

# returns True is b is a valid (col, row) coordinate and False otherwise
def validState(b):
    #check for valid column
    if(b[COL] > NUM_COLS or b[COL] < 1):
        print("belief state unknown")
        return False
    #check for valid row
    if(b[ROW] > NUM_ROWS or b[ROW] < 1):
        print("belief state unknown")
        return False
    #check if blacked out square
    if(b[0] == 2 and b[1] == 2):
        print("belief state unknown")
        return False
    return True

#If b is valid state sets p(b) to 1 and all others to 0
#Otherwise, sets all valid states to equal probability
def initBeliefs(b):
    #default for no observation
    p = 1/VALID_STATES
    bs = [[p, p, p, p],
          [p, 0.0, p, 0.0],
          [p, p, p, 0.0]]
    #check for valid observation
    if(validState(b)):
      print("state is known: ")
      print(b)
      bs = [[0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0]]
      bs[b[ROW]-1][b[COL]-1] = 1
    return bs

#prints belief array in order as defined in the lecture slides.
def printBS(bs):
    print("r:3 " + str(bs[2]))
    print("r:2 " + str(bs[1]))
    print("r:1 " + str(bs[0]))
    print("    c:1,2,3,4")
    return

# calling main function with each test case where
print("case 1")
BS = pomdp(["up", "up", "up"], [2,2,2])
printBS(BS);
#print("case 2")
#BS = pomdp(["up", "up", "up"], [1,1,1])
#printBS(BS);
#print("case 3")
#BS = pomdp(["right", "right", "up"], [1,1,"end"], [2,3])
#printBS(BS)
#print("case 4")
#BS = pomdp(["up", "right", "right", "right"], [2,2,1,1], [1,1])
#printBS(BS)

