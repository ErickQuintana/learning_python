#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
units = []
#Create your list of integers/floating-point numnbers making sure to covert from strings
for i in sys.argv[1:]:
    units.append(float(i))
print('Count:',len(units))
units.sort()
print('Minimum:',units[0])
print('Maximum:',units[-1])
#Using our list of mubers, we want to compute various stats
mean = 0
for j in range(len(units)):
    mean = mean + units[j]
print('Mean:',mean/len(units))

rmean = (mean/len(units))
standard = 0
for std in range(len(units)):
    standard = (units[std]-rmean)**2 + standard
print('Std.dev:',math.sqrt(standard/len(units)))
for i in units:
    mid = len(units)//2
    if len(units) % 2 == 1:
        median = units[mid]
    else:
        median = (units[mid]+units[mid-1])/2
print('Median:',median)
 
    
"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
