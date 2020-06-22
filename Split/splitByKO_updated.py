import sys
from Bio import Phylo

if len(sys.argv) != 3:
        print 'usage: python splitByKO.py inputFile outputDir'
        exit(1)

inputFile=sys.argv[1]
dir=sys.argv[2]

ko_array=[]

f=open(inputFile,'r')

# Each unique predicted KO becomes a cluster
for line in f:
    predicted_ko=line.split('\t\t')[0]
    if (predicted_ko not in ko_array):
        ko_array.append(predicted_ko)

# for each cluster
for ko in ko_array:
    f = open(inputFile,'r')
    for line in f:
        predicted_ko=line.split('\t\t')[0]
        truth_ko=line.split('\t\t')[1]
        solo_truth_ko=truth_ko.rsplit('_',1)[1]
        # only include in the cluster if either predicted
        #  or truth KO matches the cluster
        if (predicted_ko==ko or solo_truth_ko==ko):
            # positive: predictedKO == cluster
            # negative: predictedKO != cluster
            if (predicted_ko==ko):
                p_n='Positive'
            else:
                p_n='Negative'
            # true: predictedKO == truthKO
            # false: predictedKO != truthKO
            if (predicted_ko==solo_truth_ko):
                t_f = 'True'
            else:
                t_f = 'False'
            evalue=line.split('		')[2]
            file_path=dir
            file_path+='/'
            file_path+=ko
            f = open(file_path, "a+")
            to_write=predicted_ko
            to_write+=('            ')
            to_write+=truth_ko
            to_write+=('            ')
            to_write+=t_f
            to_write+=('            ')
            to_write+=p_n
            to_write+=('            ')
            to_write+=evalue
            f.write(to_write)
            f.write('\n')
            f.close()
