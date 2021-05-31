#!/usr/bin/env python3

import argparse
import mcb185
import random
# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

parser = argparse.ArgumentParser(description = "This program will explore the open reading drame in a sequence")
parser.add_argument('--size', required=False, type=int, default=4500000,
	metavar='<str>', help='optional size of the genome [%(default)i]')
parser.add_argument('--min_orf', required=False, type=int, default=100,
	metavar='<int>', help='Minimum open reading frame size [%(default)i]')
parser.add_argument('--gc', required=False, type=float, default=.5,
	metavar='<float>', help='GC fraction [%(default).3f]')
# switches
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
# finalization
arg = parser.parse_args()


if arg.info:print(arg.size,arg.min_orf,arg.gc)

if arg.seed:random.seed(1)
seq = mcb185.randseq(arg.size,arg.gc)
print(seq)

#Looking for an ATG 
length = []
for i in range(len(seq)-2):
    start = None
    stop = None
    if seq[i:i+3] == 'ATG':
        start = i
        for j in range(i,len(seq)-2,3):
            codon = seq[j:j+3]
            if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                stop = j
                break
    if stop != None: length.append((stop-start)/3)
print(length)