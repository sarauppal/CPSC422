#!/usr/bin/python
#CONSTANTS
NUM_COLS = 4
NUM_ROWS = 3
VALID_STATES = 9
COL = 0
ROW = 1
#Observation Models P(e | state)
#obs 1 wall
OBS_1WL = [[0.1, 0.1, 0.9, 0.1],[0.1, 0.0, 0.9, 0.0],[0.1, 0.1, 0.9, 0.0]]
#obs 2 wall
OBS_2WL = [[0.9, 0.9, 0.1, 0.9],[0.9, 0.0, 0.1, 0.0],[0.9, 0.9, 0.1, 0.0]]
#obs end
OBS_END = [[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 1.0],[0.0, 0.0, 0.0, 1.0]]
OBS_MODEL = [OBS_END, OBS_1WL, OBS_2WL]
#[currentState][previousState] = P(currentState | action, previousState)
#state = [col, row]
#[col][row][action][]
#source https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
TRANSFORMATION = []
w, h = NUM_ROWS+1, NUM_COLS+1;
TRANSFORMATION = [[0 for x in range(w)] for y in range(h)] 
TRANSFORMATION[1][1] = {"up":    [[[1,2], 0.0], [[1,1], 0.1], [[2,1], 0.1]], 
                        "down":  [[[1,2], 0.8], [[1,1], 0.9], [[2,1], 0.1]], 
                        "left":  [[[1,2], 0.1], [[1,1], 0.9], [[2,1], 0.8]], 
                        "right": [[[1,2], 0.1], [[1,1], 0.1], [[2,1], 0.0]]
                       }
TRANSFORMATION[1][2] = {"up":   [[[1,1], 0.8], [[1,2], 0.2], [[1,3], 0.0]], 
                        "down": [[[1,1], 0.0], [[1,2], 0.2], [[1,3], 0.8]], 
                        "left": [[[1,1], 0.1], [[1,2], 0.8], [[1,3], 0.1]], 
                        "right": [[[1,1], 0.1], [[1,2], 0.8], [[1,3], 0.1]]
                       }
TRANSFORMATION[1][3] = {"up":   [[[1,2], 0.8], [[1,3], 0.9], [[2,3], 0.1]], 
                        "down": [[[1,2], 0.0], [[1,3], 0.1], [[2,3], 0.1]], 
                        "left": [[[1,2], 0.1], [[1,3], 0.9], [[2,3], 0.8]], 
                        "right": [[[1,2], 0.1], [[1,3], 0.1], [[2,3], 0.0]]
                       }
TRANSFORMATION[2][1] = {"up":   [[[1,1], 0.1], [[2,1], 0.8], [[3,1], 0.1]], 
                        "down": [[[1,1], 0.1], [[2,1], 0.8], [[3,1], 0.1]], 
                        "left": [[[1,1], 0.0], [[2,1], 0.2], [[3,1], 0.8]], 
                        "right":[[[1,1], 0.8], [[2,1], 0.2], [[3,1], 0.0]]
                       }
TRANSFORMATION[2][3] = {"up":   [[[1,3], 0.1], [[2,3], 0.8], [[3,3], 0.1]], 
                        "down": [[[1,3], 0.1], [[2,3], 0.8], [[3,3], 0.1]], 
                        "left": [[[1,3], 0.0], [[2,3], 0.2], [[3,3], 0.8]], 
                        "right":[[[1,3], 0.8], [[2,3], 0.2], [[3,3], 0.0]]
                       }
TRANSFORMATION[3][1] = {"up":   [[[2,1], 0.1], [[3,1], 0.0], [[3,2], 0.0], [[4,1], 0.1]], 
                        "down": [[[2,1], 0.1], [[3,1], 0.8], [[3,2], 0.8], [[4,1], 0.1]], 
                        "left": [[[2,1], 0.0], [[3,1], 0.1], [[3,2], 0.1], [[4,1], 0.8]], 
                        "right":[[[2,1], 0.8], [[3,1], 0.1], [[3,2], 0.1], [[4,1], 0.0]]
                       }
TRANSFORMATION[3][2] = {"up":   [[[3,1], 0.8], [[3,2], 0.1], [[3,3], 0.0]], 
                        "down": [[[3,1], 0.0], [[3,2], 0.1], [[3,3], 0.8]], 
                        "left": [[[3,1], 0.1], [[3,2], 0.8], [[3,3], 0.1]], 
                        "right":[[[3,1], 0.1], [[3,2], 0.0], [[3,3], 0.1]]
                       }
TRANSFORMATION[3][3] = {"up":   [[[2,3], 0.1], [[3,3], 0.8], [[3,2], 0.8]], 
                        "down": [[[2,3], 0.1], [[3,3], 0.0], [[3,2], 0.0]], 
                        "left": [[[2,3], 0.0], [[3,3], 0.1], [[3,2], 0.1]], 
                        "right":[[[2,3], 0.8], [[3,3], 0.1], [[3,2], 0.1]]
                       },
TRANSFORMATION[4][1] = {"up":   [[[3,1], 0.1], [[4,1], 0.1]], 
                        "down": [[[3,1], 0.1], [[4,1], 0.9]], 
                        "left": [[[3,1], 0.0], [[4,1], 0.1]], 
                        "right":[[[3,1], 0.8], [[4,1], 0.9]]
                       },
TRANSFORMATION[4][2] = {"up":   [[[3,2], 0.1], [[4,1], 0.8]], 
                        "down": [[[3,2], 0.1], [[4,1], 0.0]], 
                        "left": [[[3,2], 0.0], [[4,1], 0.1]], 
                        "right":[[[3,2], 0.8], [[4,1], 0.1]]
                       },
TRANSFORMATION[4][3] = {"up":   [[[3,3], 0.1]], 
                        "down": [[[3,3], 0.1]], 
                        "left": [[[3,3], 0.0]], 
                        "right":[[[3,3], 0.8]]
                       }



# inputs:
# a: sequence of actions
# e: sequence of observations
# b: belief state [col, row], default unknown
def pomdp(a, o, b = [0, 0] ):
    beliefStateDistribution = initBeliefs(b)
    for i in range(0,len(a)):
        beliefStateDistribution = updateBeliefs(a[i], o[i], beliefStateDistribution)
    return beliefStateDistribution

def updateBeliefs(a, o, b):
    evidence = o
    newBeliefState = [[0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0], 
                      [0.0, 0.0, 0.0, 0.0]]
    if o == "end":
        evidence = 0
    for col in range(0,NUM_COLS):
        for row in range(0,NUM_ROWS):
            print("col: " + str(col+1) + " row: " + str(row+1))
            print("action: " + a)
            prevStates = TRANSFORMATION[COL+1][ROW+1]
            print(prevStates)
            beliefPrevState = b[row][col]
            probOfNewStates = sumNewStateGivenAction(a, prevStates) 
            probEvidenceGivenNewState = OBS_MODEL[evidence][row][col]
            print("pof " + str(evidence) + "|[" + str(col+1) + "," + str(row+1) + "] is " + str(probEvidenceGivenNewState))
    return b

def sumNewStateGivenAction(a, prevStates):
    sum = 0
    print(prevStates[a])
    return sum

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
print("case 2")
BS = pomdp(["up", "up", "up"], [1,1,1])
printBS(BS);
print("case 3")
BS = pomdp(["right", "right", "up"], [1,1,"end"], [2,3])
printBS(BS)
print("case 4")
BS = pomdp(["up", "right", "right", "right"], [2,2,1,1], [1,1])
printBS(BS)

