#!/usr/bin/env python3

import argparse
import mcb185
import statistics
# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library

parser = argparse.ArgumentParser(description = "This program will calculate the GC content on a sliding sindow")
parser.add_argument('--file', required=True, type =str, metavar= '<str>', help="require Fasfa file")
arg = parser.parse_args()

Dna_len = []
for name, seq in mcb185.read_fasta(arg.file):
    Dna_len.append(len(seq))
Dna_len.sort()
print(Dna_len)

#To find the Minimum length of al the seqeunces
print('Minimum is',Dna_len[0])

print('Maximum is',Dna_len[-1])
#This is to find the sum of al the seqeunces
total = 0
 
for i in Dna_len:
     total += i
print('The sum is',total)

print('mean is', statistics.mean(Dna_len))
print('median is', statistics.median(Dna_len))

print('The N50 is',mcb185.n502(Dna_len))
