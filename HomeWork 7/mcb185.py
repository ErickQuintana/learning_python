import random
#start = "ATG" # package varaibles

def read_fasta(filename):
	name = None
	seq = []
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][1:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)
	
def rev_comp(seq):
	rc = ""
	for nt in seq[::-1]:
		if nt == "A": rc += "T"
		elif nt == "T": rc += "A"
		elif nt == "C": rc += "G"
		elif nt == "G": rc += "C"
	return rc

def gc(dna):
    g= dna.count("G")
    c= dna.count("C")
    return (g+c)/len(dna)


def n50(Dna_len) :
	running_sum = 0
	total = sum(Dna_len)
	for i in Dna_len:
		running_sum += i
		if running_sum > total/2:
 			return i


def n502(seq):
	seq.sort()
	running_sum = 0
	total = sum(seq)
	i = 0
	while running_sum < total/2:
		running_sum += seq[i]
		i += 1
	return seq[i]
#seq = mcb185.randseq(arg.size,arg.gc_fraction)	
def randseq(length,gc):
	seq = ''
	for i in range(length):
		if random.random() < gc:
			seq += random.choice("GC")
		else:
			seq += random.choice("AT")
	return seq
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}	
def translate(seq):
	seq = seq.upper() #makes the entire seq consist of upper case letters
	protein = ''
	for nt in range(0,len(seq)-2,3):
		codon = seq[nt:nt+3]
		if codon in gcode:
			protein += gcode[codon]
		else:
			protein += X
	return protein

     