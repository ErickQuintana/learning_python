#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
randdna = 30
seq = ""
ATcontent = 0
for i in range(randdna):
    nts = random.choice("AAACCGGTTT")
    seq += nts
    if seq[i] == 'A' or seq[i] == "T":
            ATcontent += 1
print(len(seq), ATcontent/len(seq),seq, "sequnce 1")

newranddna = 30
seq2 = ""
T = 0.6
ATcontentseq2 = 0
for i in range(newranddna):
    rn = random.random()
    if rn < T : 
        seq2 += random.choice('AT')
    else: 
         seq2 += random.choice('GC')
    if seq2[i] == "A" or seq2[i] == "T":
            ATcontentseq2 += 1
print(len(seq2), ATcontentseq2/(len(seq2)), "sequnce 2")

seq3 = ""
for i in range(randdna):
    n = random.random()
    if n < T:
        if random.random() > .5 :
            seq3 += "A"
            seq3 += "C"
        else:
            seq3 += random.choice("GC")
print(len(seq3),seq3, "sequence 3")
# I dont know why i only get a 25 nt long sequence
#First code

"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
