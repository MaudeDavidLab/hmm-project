import sys 

if len(sys.argv) != 3:
	print 'usage: python getMissing.py inputFile 10percentFile'
	exit(1)

inputFile = sys.argv[1]
percFile = sys.argv[2]

matchArray = []
KO = 0
hmmF = open(inputFile, "r")
for line in hmmF:
	seq = line.split()[0]
	if (seq != "#"):
		matchArray.append(seq)
		if (KO == 0):
			KO = line.split()[2]
hmmF.close()

outputFile = KO
outputFile += "_missing.txt"

orF = open(percFile, "r") 
out = open(outputFile, "w")
for line in orF: 
	if '>' in line: 
		newLine = line.strip()
		newLine = newLine[1:]
		if newLine not in matchArray:
			string = KO
			string += '		'
			string += newLine
			string += '		'
			string += str(100000000)
			string += '\n'
			out.write(string)
orF.close()
out.close()
