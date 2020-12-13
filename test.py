from os import sys
import itertools
string = "rRdDbB"
# provides all combinations starting with shortest length
for count in range(1, 4):
    for characters in itertools.product(string, repeat=count):
        print (''.join(characters))