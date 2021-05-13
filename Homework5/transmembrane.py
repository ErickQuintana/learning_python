#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
import sys

def kd(seq):
    Hydrophobicity = 0
    for i in range(len(seq)):
        if seq[i] == 'I':
            Hydrophobicity += 4.5
        elif seq[i] == 'V':
            Hydrophobicity += 4.2
        elif seq[i] == 'L':
            Hydrophobicity += 3.8
        elif seq[i] == 'F':
            Hydrophobicity +=  2.8
        elif seq[i] == 'C':
            Hydrophobicity += 2.5
        elif seq[i] == 'M':
            Hydrophobicity += 1.9
        elif seq[i] == 'A':
            Hydrophobicity += 1.8
        elif seq[i] == 'G':
            Hydrophobicity -= 0.4
        elif seq[i] == 'T':
            Hydrophobicity -= 0.7
        elif seq[i] == 'S':
            Hydrophobicity -= 0.8
        elif seq[i] == 'W':
            Hydrophobicity -= .9
        elif seq[i] == 'Y':
            Hydrophobicity -= 1.3
        elif seq[i] == 'P':
            Hydrophobicity -= 1.6
        elif seq[i] == 'H':
            Hydrophobicity -= 3.2
        elif seq[i] == 'E' :
            Hydrophobicity -= 3.5
        elif seq[i] == 'Q':
            Hydrophobicity -= 3.5
        elif seq[i] == 'D':
            Hydrophobicity -= 3.5
        elif seq[i] == 'N':
            Hydrophobicity -= 3.5
        elif seq[i] == 'K':
            Hydrophobicity -= 3.9
        elif seq[i] == 'R':
            Hydrophobicity -= 4.5
    return Hydrophobicity

peptide_length = 30

def Signal_peptide(seq):
    w = 8
    sp = False
    for i in range(len(seq)-len(seq)+peptide_length-w):
        aa = seq[i:i+w]
        int =kd(seq[i:i+w])
        if int > 2.5 :
            sp = True
    return sp
        
        
    




def hydrophobic(seq):
    w = 11
    hydr = False
    for i in range(peptide_length,len(seq)-w):
        int = kd(seq[i:i+w])
        aa = seq[i:i+w]
        if int > 2.0:
            hydr = True
    return hydr

def transmembrane(seq):
    hydrophobic(seq)
    if Signal_peptide(seq) == True and hydrophobic(seq) == True:
        print('Posible transmemebrane protein')



# get all sequences
ids = []
proteins = []
with open(sys.argv[1]) as fp:
    seq = []
    for lines in fp.readlines():
        lines = lines.rstrip()
        if lines.startswith( '>' ):
            words = lines.split()
            ids.append(words[0][1:])
            if len(seq) > 0 : proteins.append(''.join(seq))
            seq = []
        else:
            seq.append(lines)
    proteins.append(''.join(seq))
#print(len(ids),proteins)

# Look for hydrophobic regions in all sequences
for id,seq in zip(ids,proteins):
    print(id,len(seq))
    transmembrane(seq)


"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
