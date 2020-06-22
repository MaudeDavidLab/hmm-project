# extracts fullfasta.fasta - 10percent.fasta to get 90percent.fasta
import sys

if len(sys.argv) != 4:
	print len(sys.argv)
	print sys.argv[1]
	print sys.argv[2]
	print sys.argv[3]
	print 'usage: python 90percent.py fullSeqFile 10percentSeqFile outputFile'
	exit(1)
FULLfile = sys.argv[1]
TENpercent = sys.argv[2]
output = sys.argv[3]

file_obj=open(output,'w+')
file_obj2=open(FULLfile,'r')
matched=0
for line in file_obj2:
    if line[0]=='>':
        with open(TENpercent, 'r') as f:
            for cline in f:
                if cline[0]=='>':
                    if cline==line:
                        matched=1
                        break
                    elif cline!=line:
                        matched=0
        if matched==0:
            file_obj.write(line)
    else:
        if matched==0:
            file_obj.write(line)
file_obj.close()
file_obj2.close()
