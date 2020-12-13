#! python3
# cubeSolver.py - A program to find shortest algorithm to solve the 
# 2x2 rubiks cube
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

def generateAlg(cube1=scrambledCube, cube2=solvedCube):
    # provides all combinations starting with shortest length
    for count in range(1, 8):
        print(f"Depth {count}...")
        for characters1 in itertools.product("rRdDbB", repeat=count):
            alg1 = ''.join(characters1)
            copyScrambled = copy.deepcopy(scrambledCube)
            performAlg(copyScrambled, alg1)
            if count == 1:
                if isMatch(copyScrambled, cube2):
                    print(f"Found: {alg1}")
                    sys.exit()
                for characters2 in itertools.product("rRdDbB", repeat=count):
                    alg2 = ''.join(characters2)
                    copySolved = copy.deepcopy(solvedCube)
                    performAlg(copySolved, alg2)
                    if isMatch(copyScrambled, copySolved):
                        print(f"Found: {alg1}{alg2.swapcase()[::-1]}")
                        sys.exit()
            else:
                for characters2 in itertools.product("rRdDbB", repeat=count-1):
                    alg2 = ''.join(characters2)
                    copySolved = copy.deepcopy(solvedCube)
                    performAlg(copySolved, alg2)
                    if isMatch(copyScrambled, copySolved):
                        print(f"Found: {alg1}{alg2.swapcase()[::-1]}")
                        sys.exit()
                for characters2 in itertools.product("rRdDbB", repeat=count):
                    alg2 = ''.join(characters2)
                    copySolved = copy.deepcopy(solvedCube)
                    performAlg(copySolved, alg2)
                    if isMatch(copyScrambled, copySolved):
                        print(f"Found: {alg1}{alg2.swapcase()[::-1]}")
                        sys.exit()
generateAlg()