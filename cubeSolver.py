#! python3
# cubeSolver.py - A program to find algorithms to solve a 
# 2x2 rubiks cube
# printed result will be as if a 2d cube was flattened
# lower case == clockwise, upper case == counter-clockwise

from helper import *
from os import sys
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

def generateAlgs(alg="", cube1=scrambledCube, cube2=solvedCube):
        for letter in "rRdDbB":
            alg1 = alg + letter
            cubeCopy = copy.deepcopy(scrambledCube)
            performAlg(cubeCopy, alg1)
            if isMatch(cubeCopy, solvedCube):
                print(alg1)
                sys.exit()
        for letter in "rRdDbB":
            generateAlgs(alg+letter)
generateAlgs()