import random

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
	
	        