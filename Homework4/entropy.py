#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys
p = [] #this is an empty list/conmtainter that will contain our propbabilties that were inputted into terminal
for s in sys.argv[1:]:
    p.append(float(s))

print(p)
H = 0
for i in range(len(p)):
    H-= p[i] * math.log2(p[i])
print(H)
"""
python3 entropy.py 0.1 0.2 0.3 0.4
1.846

for i in range(1, len(sys.argv)): #this is syaing starting at 1 through the length of sys.argv(which is inputs from the command line  in the form of strings)
    p.append(float(sys.argv[i]))#here we convert the sys.argv strings into float and puts it in a list. in other words we are pulling every elemnent out of the list adn then append the floating version of that
"""
