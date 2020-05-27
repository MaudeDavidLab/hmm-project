import sys

if len(sys.argv) != 3:
	print("Usage: python format.py <inputFile> <outputFile>")
	sys.exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]
file_obj = open(inputFile, "r")
file_obj2 = open(outputFile, "w")



with open(inputFile, "r") as f:
	for line in f:
		if line[0]== '>':
			first=line.split(' ')[0]
			second=line.split(' ')[1]
			first+='_'		
			if second == 'no':
				first+=second
				second=line.split(' ')[2]
				first+='_'
				first+=second
			else:
				first+=second
			first+='\n'
			file_obj2.write(first)
		else:
			file_obj2.write(line)
			
