#! python3
# cubeSolver.py - A program to find algorithms to solve a 
# 2x2 rubiks cube
# printed result will be as if a 2d cube was flattened
# lower case == clockwise, upper case == counter-clockwise

from helper import *
import copy

# make a scrambled cube
scrambledCube = copy.deepcopy(solvedCube)

# print solved cube to screen
printCube(solvedCube)
print()

# ask user for algorithm to scramble cube with
print("Please provide algorithm to scramble cube")
print("Notation to use:")
print("r = right clockwise")
print("R = right anit-clockwise")
print("d = down clockwise")
print("D = down anit-clockwise")
print("b = back clockwise")
print("B = back anit-clockwise")

while True:
    scramble = input("Algorithm: ")
    valid = True
    for letter in scramble:
        if letter not in "rRbBdD":
            valid = False
    if valid:
        break

# scramble cube
scrambler(scrambledCube, scramble)

# print scrambled cube to screen
print()
printCube(scrambledCube)

# list of algorithms used
algorithms = []

# search for algorithms - max 11 moves
def searchAlgs(scrambledCube, solvedCube, edgeCounter=0, prevMove="", alg="", algList=algorithms):
    # create max 11 case
    if edgeCounter == 8:
        return
    # create base case
    if isMatch(scrambledCube, solvedCube):
        algList.append(alg)
        return
    # prevMove prevents redundant moves
    if prevMove != "R":
        cubePath1 = copy.deepcopy(scrambledCube)
        rightTurn(cubePath1)
        algPath1 = alg + "r"
        counter1 = edgeCounter + 1
        searchAlgs(cubePath1, solvedCube, counter1, "r", algPath1)
    # prevMove prevents redundant moves
    if prevMove != "r":
        cubePath2 = copy.deepcopy(scrambledCube)
        rightTurn(cubePath2, False)
        algPath2 = alg + "R"
        counter2 = edgeCounter + 1
        searchAlgs(cubePath2, solvedCube, counter2, "R", algPath2)
    # prevMove prevents redundant moves
    if prevMove != "B":
        cubePath3 = copy.deepcopy(scrambledCube)
        backTurn(cubePath3)
        algPath3 = alg + "b"
        counter3 = edgeCounter + 1
        searchAlgs(cubePath3, solvedCube, counter3, "b", algPath3)
    # prevMove prevents redundant moves
    if prevMove != "b":
        cubePath4 = copy.deepcopy(scrambledCube)
        backTurn(cubePath4, False)
        algPath4 = alg + "B"
        counter4 = edgeCounter + 1
        searchAlgs(cubePath4, solvedCube, counter4, "B", algPath4)
    # prevMove prevents redundant moves
    if prevMove != "D":
        cubePath5 = copy.deepcopy(scrambledCube)
        bottomTurn(cubePath5)
        algPath5 = alg + "d"
        counter5 = edgeCounter + 1
        searchAlgs(cubePath5, solvedCube, counter5, "d", algPath5)
    # prevMove prevents redundant moves
    if prevMove != "d":
        cubePath6 = copy.deepcopy(scrambledCube)
        bottomTurn(cubePath6, False)
        algPath6 = alg + "D"
        counter6 = edgeCounter + 1
        searchAlgs(cubePath6, solvedCube, counter6, "D", algPath6)

searchAlgs(scrambledCube, solvedCube)

# sort algorithm list from smalled to biggest
algorithms.sort()
# print algorithms to screen
print(algorithms)
