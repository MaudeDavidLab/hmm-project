# gets all the colored branches from a phyloxml file and divies them 
#    up into ko files 
import sys
from Bio import Phylo
from Bio import SeqIO

if len(sys.argv) != 4:
	print 'usage: python splitToFile.py inputXMLfile outputDir 90percentFastaFile'
	exit(1)

file=sys.argv[1]
dir=sys.argv[2]
fasta=sys.argv[3]
tree = Phylo.read(file, 'phyloxml')

ko_array=[]
name_array=[]

for clade in tree.get_terminals():
    red=clade.color.red
    blue=clade.color.blue
    green=clade.color.green
    if not (red==255 and blue==0 and green==0):
        ko=clade.name.rsplit('_',1)[1]
	#print ko
        #print clade.name, clade.color
        if ko not in ko_array and len(ko)>2:
            ko_array.append(ko)
        name_array.append(clade.name)

records=[]
for record in SeqIO.parse(fasta, "fasta"):
	records.append(record.id)
new_name_dict = {}
key = 0
for i in name_array:
	hold = i
	if '_P_' in i: 
		i = i.split('_P_')[0]
	for k in records:
		if i in k:
			arr = []	
			arr.append(hold)
			arr.append(k) 
			new_name_dict.update({key:arr})
			key+=1

record_dict = SeqIO.index(fasta, "fasta")

for i in ko_array:
    file_path=dir
    file_path+='/'
    file_path+=i
    f = open(file_path, "w+")
    key = 0			
    for k in new_name_dict:
        if i in new_name_dict.get(k)[0]:
		strr = '>'
		strr+= new_name_dict.get(k)[0]
		strr+='\n'
		f.write(strr)
		strr = str(record_dict[new_name_dict.get(k)[1]].seq)
		strr+='\n'
		f.write(strr)
#		x = record_dict.get_raw(k).decode()).seq
	key+=1
    f.close()
