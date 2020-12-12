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
print()
# list of algorithms used
algorithms = []

# search for algorithms - max 11 moves
def searchAlgs(cube1, cube2, prevMove1="", prevMove2="", alg1="", alg2="", edgeCounter=0, algList=algorithms):
    # create max 11 case
    if edgeCounter == 7:
        return
    # create base case
    if isMatch(cube1, cube2):
        algList.append(alg1 + alg2.swapcase()[::-1])
        return
    
    # determines which cube to permutate next
    if edgeCounter % 2 != 0:
        prevMove = prevMove2
        secondCube = True
    else:
        prevMove = prevMove1
        secondCube = False

    # prevMove prevents redundant moves
    if prevMove != "R":
        if secondCube:
            cubePath1 = copy.deepcopy(cube2)
            algPath1 = alg2 + rightTurn(cubePath1)
            searchAlgs(cube1, cubePath1, prevMove1, "r", alg1, algPath1, edgeCounter + 1)
        else:
            cubePath1 = copy.deepcopy(cube1)
            algPath1 = alg1 + rightTurn(cubePath1)
            searchAlgs(cubePath1, cube2, "r", prevMove2, algPath1, alg2, edgeCounter + 1)
    # prevMove prevents redundant moves
    if prevMove != "r":
        if secondCube:
            cubePath2 = copy.deepcopy(cube2)
            algPath2 = alg2 + rightTurn(cubePath2, False)
            searchAlgs(cube1, cubePath2, prevMove1, "R", alg1, algPath2, edgeCounter + 1)
        else:
            cubePath2 = copy.deepcopy(cube1)
            algPath2 = alg1 + rightTurn(cubePath2, False)
            searchAlgs(cubePath2, cube2, "R", prevMove2, algPath2, alg2,  edgeCounter + 1)
    # prevMove prevents redundant moves
    if prevMove != "B":
        if secondCube:
            cubePath3 = copy.deepcopy(cube2)
            algPath3 = alg2 + backTurn(cubePath3)
            searchAlgs(cube1, cubePath3, prevMove1, "b", alg1, algPath3, edgeCounter + 1)
        else:
            cubePath3 = copy.deepcopy(cube1)
            algPath3 = alg1 + backTurn(cubePath3)
            searchAlgs(cubePath3, cube2, "b", prevMove2, algPath3, alg2, edgeCounter + 1)
    # prevMove prevents redundant moves
    if prevMove != "b":
        if secondCube:
            cubePath4 = copy.deepcopy(cube2)
            algPath4 = alg2 + backTurn(cubePath4, False)
            searchAlgs(cube1, cubePath4, prevMove1, "B", alg1, algPath4, edgeCounter + 1)
        else:
            cubePath4 = copy.deepcopy(cube1)
            algPath4 = alg1 + backTurn(cubePath4, False)
            searchAlgs(cubePath4, cube2, "B", prevMove2, algPath4, alg2, edgeCounter + 1)
    # prevMove prevents redundant moves
    if prevMove != "D":
        if secondCube:
            cubePath5 = copy.deepcopy(cube2)
            algPath5 = alg2 + bottomTurn(cubePath5)
            searchAlgs(cube1, cubePath5, prevMove1, "d", alg1, algPath5, edgeCounter + 1)
        else:
            cubePath5 = copy.deepcopy(cube1)
            algPath5 = alg1 + bottomTurn(cubePath5)
            searchAlgs(cubePath5, cube2, "d", prevMove2, algPath5, alg2, edgeCounter + 1)
    # prevMove prevents redundant moves
    if prevMove != "d":
        if secondCube:
            cubePath6 = copy.deepcopy(cube2)
            algPath6 = alg2 + bottomTurn(cubePath6, False)
            searchAlgs(cube1, cubePath6, prevMove1, "D", alg1, algPath6, edgeCounter + 1)
        else:
            cubePath6 = copy.deepcopy(cube1)
            algPath6 = alg1 + bottomTurn(cubePath6, False)
            searchAlgs(cubePath6, cube2, "D", prevMove2, algPath6, alg2, edgeCounter + 1)

searchAlgs(scrambledCube, solvedCube)

# sort algorithm list from smalled to biggest
algorithms.sort(key=lambda e : len(e))
print(algorithms)
