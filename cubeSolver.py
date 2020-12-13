#! python3
# cubeSolver.py - A program to find algorithms to solve a 
# 2x2 rubiks cube
# printed result will be as if a 2d cube was flattened
# lower case == clockwise, upper case == counter-clockwise

from helper import *
from os import sys
import copy, itertools

# make a scrambled cube
scrambledCube = copy.deepcopy(solvedCube)

# print solved cube to screen
printCube(solvedCube)
print()

# ask user for algorithm to scramble cube with
print("Please provide algorithm to scramble cube")
print("Notation to use:")
print("r = right clockwise")
print("R = right anti-clockwise")
print("d = down clockwise")
print("D = down anti-clockwise")
print("b = back clockwise")
print("B = back anti-clockwise")

while True:
    scramble = input("Algorithm: ")
    valid = True
    for letter in scramble:
        if letter not in "rRbBdD":
            valid = False
    if valid:
        break

# scramble cube
performAlg(scrambledCube, scramble)

# print scrambled cube to screen
print()
printCube(scrambledCube)
print()
# list of algorithms used

def generateAlgs(cube1=scrambledCube, cube2=solvedCube):
    # provides all combinations starting with shortest length
    for count in range(1, 15):
        for characters in itertools.product("rRdDbB", repeat=count):
            algorithm = ''.join(characters)
            copyCube = copy.deepcopy(scrambledCube)
            performAlg(copyCube, algorithm)
            if isMatch(copyCube, cube2):
                print(algorithm)
                sys.exit()

generateAlgs()