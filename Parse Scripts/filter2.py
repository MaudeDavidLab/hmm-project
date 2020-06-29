import sys 
import os 

if len(sys.argv) != 4:
	print ('usage: python filter2.py pfamName numSeq percentage')
	exit(1)

pfamName = sys.argv[1]
numSeq = sys.argv[2]
percentage = sys.argv[3]

#num=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
num=['one']
newMainDir = pfamName
newMainDir += '/threshold_'
newMainDir += numSeq 
newMainDir += '_percentage_'
newMainDir += percentage

os.mkdir(newMainDir)

# creates directories 
for x in num: 
	os.mkdir(newMainDir+'/'+x)
	os.mkdir(newMainDir+'/'+x+'/'+'finalDir')
	os.mkdir(newMainDir+'/'+x+'/'+'finalDir/90percentKO')
	os.mkdir(newMainDir+'/'+x+'/'+'finalDir/alignedFiles')
	os.mkdir(newMainDir+'/'+x+'/'+'finalDir/hmmProfiles')
	os.mkdir(newMainDir+'/'+x+'/'+'finalDir/hmmSearchOut')

# copies over only the clusters with at least numSeq sequences
for x in num:
	dr = pfamName
	dr += '/'
	dr += x
	dr += '/finalDir/90percentKO/'

	for filename in os.listdir(dr):
		currFile = dr
		currFile += filename

		command = 'cat '
		command += currFile
		command += ' | grep ">"|wc -l'
		stream = os.popen(command)
		output = stream.read()
	
		if int(output) >= int(numSeq):
			command = 'cp '
			command += currFile
			command += ' ' 
			command += newMainDir + '/' + x  + '/finalDir/90percentKO/'
			os.system(command) 

# removes the prpagated sequences when clusters that contain less than the percentage annotated sequences
for x in num: 
	dr = newMainDir
	dr += '/'
	dr += x
	dr += '/finalDir/90percentKO/'
	
	for filename in os.listdir(dr):
		currFile = dr
		currFile += filename
		
		command = 'cat '
		command += currFile
		command += ' | grep ">"|wc -l'
		stream = os.popen(command)
		totalSequences = stream.read()

		command = 'cat '
		command += currFile 
		command += ' | grep "_P_"|wc -l'
		stream = os.popen(command)
		propagatedSequences = stream.read()
		annotatedSequences = int(totalSequences) - int(propagatedSequences)
		percentageAnnotated = int(annotatedSequences)/int(totalSequences)
	 		
		# if less remove the propagated sequences 
		if float(percentageAnnotated) < float(percentage):
			copy = 1
			r = open(currFile, 'r')
			w = open(currFile+'_temp', 'w+')
			for line in r:
				if '>' in line:
					if '_P_' in line: 
						copy=1
					else: 
						w.write(line)
						copy=0
				else: 
					if copy==0: 
						w.write(line)
			os.system('rm -f '+ currFile)
			os.system('mv ' + currFile+'_temp ' + currFile)
			r.close()
			w.close() 

# now just follow the old pipeline

# align each of the KO files
for x in num: 
	dr = newMainDir
	dr += '/'
	dr += x
	dr += '/finalDir/90percentKO/'
	for filename in os.listdir(dr):
		command = 'clustalw2 ' + dr+filename
		os.system(command)

# move aligned files over to /alignedFiles
for x in num: 
	dr = newMainDir
	dr += '/'
	dr += x
	prDr = dr + '/finalDir/90percentKO/'
	
	alDir = dr + '/finalDir/alignedFiles/'
	command = 'mv ' + prDr+'/*.aln ' + alDir
	os.system(command)

# build hmmprofiles for the aligned files 
for x in num: 
	dr = newMainDir
	dr += '/'
	dr += x
	adr = dr + '/finalDir/alignedFiles/'
	pdr = dr + '/finalDir/hmmProfiles/'

	for filename in os.listdir(adr):
		command = 'hmmbuild ' + pdr+filename +'.hmm ' + adr+filename
		os.system(command)

# copies over original10.fasta and getRes.py
for x in num:
	dr = pfamName
	dr += '/'
	dr += x
	dr += '/finalDir/original10.fasta'

	command = 'cp ' + dr + ' ' + newMainDir+'/'+x+'/finalDir/'
	os.system(command) 

	
	dr = pfamName
	dr += '/'
	dr += x + '/getRes.py'
	command = 'cp ' + dr + ' ' + newMainDir+'/'+x+'/'
	os.system(command) 

# hmmsearch
for x in num: 
	dr = newMainDir
	dr += '/'
	dr += x
	dr += '/finalDir/hmmProfiles/'
	
	for filename in os.listdir(dr):
		command = 'hmmsearch -E 10000000000000000000000000 --max --tblout '
		command += newMainDir + '/' + x + '/finalDir/hmmSearchOut/' + filename + ' ' 
		command += dr+filename + ' ' + newMainDir+'/'+x+'/finalDir/original10.fasta'
		os.system(command)

# gets all the files with hits 
for x in num: 
	dr = newMainDir 
	dr += '/'
	dr += x
	dr += '/finalDir/hmmSearchOut/'
	
	for filename in os.listdir(dr):
		command = 'wc -l ' + dr+filename
		stream = os.popen(command)
		output = stream.read()
		output = output.split(' ')[0]

		if int(output) == 13: 
			command = 'rm -f ' + dr+filename
			os.system(command)
# get the missing sequences
for x in num: 
	dr = newMainDir 
	dr += '/'
	dr += x
	odr = dr + '/finalDir/hmmSearchOut/'
	
	for filename in os.listdir(odr):
		inputFile = odr + filename
		percFile = newMainDir+'/'+x+'/finalDir/original10.fasta'
		
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
		outputFile = dr + '/' + KO
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

# generates the table at each fold
for x in num: 
	dr = newMainDir 
	dr += '/'
	dr += x
	odr = dr + '/finalDir/hmmSearchOut/'

	command = 'touch ' 
	command += dr + '/results'
	os.system(command)
	for filename in os.listdir(odr):
		command = 'python ' + dr + '/getRes.py ' + odr + filename + ' ' + dr + '/results'
		os.system(command)

# adds the missing sequences to the results table
for x in num: 
	dr = newMainDir 
	dr += '/'
	dr += x
	dr += '/'
	
	for filename in os.listdir(dr):
		if '_missing.txt' in filename: 
			command = 'cat ' + dr + filename + ' >> ' + dr + 'results' 

# Get a master results table
command = 'touch ' + newMainDir + '/master_results'
os.system(command)
for x in num: 
	command = 'awk \'FNR>1\' ' + newMainDir  + '/' + x + '/results >> ' + newMainDir + '/master_results'
	os.system(command) 
	
# copies splitByKO_updated.py and remove_no_KO.py over
command = 'cp ' + pfamName + '/splitByKO_updated.py ' + newMainDir + '/'
os.system(command) 

command = 'cp ' + pfamName + '/remove_no_KO.py ' + newMainDir + '/'
os.system(command) 

# Split master res based on KO
os.mkdir(newMainDir + '/KO_fin')
command = 'python ' + newMainDir + '/splitByKO_updated.py ' + newMainDir + '/master_results ' + newMainDir + '/KO_fin'
os.system(command) 

# Remove no KO
os.mkdir(newMainDir + '/KO_FIN_noKO_gone')
command = 'python ' + newMainDir + '/remove_no_KO.py ' + newMainDir + '/KO_fin ' + newMainDir + '/KO_FIN_noKO_gone'
os.system(command) 
