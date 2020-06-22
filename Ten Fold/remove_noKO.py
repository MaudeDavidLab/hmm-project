# removes the no_ko
import sys

if len(sys.argv) != 3:
	print 'usage: python remove_noKO inputFile outFile'
	exit(1)

inputFile = open(sys.argv[1], 'r')
outputFile = sys.argv[2]

outfile=open(outputFile, 'w+')

pri=1

for line in inputFile:
	if line[0]=='>':
		if (len(line.rsplit('_'))==5):
			if not line.rsplit('_')[3] == 'no':
				pri=1
				outfile.write(line)
			else:
				pri=0
        
		elif (len(line.rsplit('_'))==4):
			if not line.rsplit('_')[2] == 'no':
				pri=1
				outfile.write(line)
			else:
				pri=0
		elif (len(line.rsplit('_'))==3):
			if not line.rsplit('_')[1] == 'no':
				pri=1
				outfile.write(line)
			else:
				pri=0
		elif (len(line.rsplit('_'))==2):
			pri=1
			outfile.write(line)
	else:
		if pri==1:
			outfile.write(line)
