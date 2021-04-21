#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
antidna = ''

for i in range(len(dna)-1, -1, -1) :
    nt = dna[i]
    if nt == "A" :
        antidna += "T"
    elif nt == "T" :
        antidna += "A"
    elif nt == "C" :
        antidna += "G"
    elif nt == "G" :
        antidna += "C"
    else: antidna += "N"

print(antidna)


"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
