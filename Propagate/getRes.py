import sys
from Bio import SearchIO

if len(sys.argv) != 3:
	print 'usage: python getRe.py inputFile outFile'
	exit(1)

inputFile = open(sys.argv[1], 'r')
outputFile = sys.argv[2]
	
count = len(open(outputFile).readlines(  ))
output = open(outputFile,'a')
if count<1:
	output.write( 'predicted		truth			evalue			match\n')
r=SearchIO.read(inputFile, 'hmmer3-tab')
print(inputFile)
for hit in r:
	output.write(r.id)
	output.write('		')
	output.write(hit.id)
	output.write('		')
	output.write(str(hit.evalue))
	output.write('		')
	hitsplit=hit.id.rsplit('_')
	koOnly=hitsplit[len(hitsplit)-1]
	if r.id==koOnly:
		output.write("True")
	else:
		output.write("False")
	output.write('\n')
