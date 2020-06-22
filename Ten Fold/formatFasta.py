# code retrieved from:https://www.biostars.org/p/205745/#205917

import sys
inputfile = sys.argv[1]
outputFile='temp100030232'
length = int(sys.argv[2])

#outfile = open(inputfile.split(".fasta")[0] + '_multi-line.fasta', 'w') #open outfile for writing
outfile = open(outputFile, 'w')
with open(inputfile, 'r') as f:
     for line in f:
        if line.startswith(">"):
                print >> outfile, line.strip()
        else:
                sequence = line.strip()
                while len(sequence) > 0:
                        print >>outfile, sequence[:length]
                        sequence = sequence[length:]
