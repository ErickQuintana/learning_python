#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
#Create Your variables 
genm_sz = int(sys.argv[1])
rdnum =  int(sys.argv[2])
rdlen = int(sys.argv[3])
#how will you get your random read coverade using random.random
chrm = []
for i in range(genm_sz):
    chrm.append(0)
#print(chrm)
for i in range(rdnum):
    position = random.randint(0,genm_sz-rdlen)
    for j in range(rdlen):
        chrm[position+j] += 1
max = chrm[rdlen]
min = chrm[rdlen]
total = 0
for v in chrm[rdlen:-rdlen]:
    if v < min:
        min = v
    if v > max :
        max = v
    total += v
print(chrm, min,max, total/(genm_sz-2*rdlen))
    

     
    

"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
