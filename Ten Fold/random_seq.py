# this file grabs a certain number of random sequences from a file 

import sys

if len(sys.argv) != 4:
	print 'usage: python random_seq.py FullSeqFile outputFile numSeq'
	exit(1)

inputFile = sys.argv[1]
outputFile = open(sys.argv[2], 'w+')
numSeq = sys.argv[3]

from Bio import SeqIO
from random import sample
with open(inputFile) as f:
    seqs = SeqIO.parse(f, "fasta")
    samps = ((seq.name, seq.seq) for seq in  sample(list(seqs),int(numSeq)))
    for samp in samps:
        outputFile.write(">{}\n{}".format(*samp))
outputFile.close()
