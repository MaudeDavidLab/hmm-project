import os
import requests
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) != 4:
    print("Usage: python getgenes_UPDATED.py <name> <outputFileName> <geneAbrFile>")
    sys.exit()

name = sys.argv[1]
outFile = sys.argv[2]
proFile = sys.argv[3]
prok_seqFile = outFile.split(".")[0] + "_prok.txt"
errorFile = outFile.split(".")[0] + "_ErrorFile.txt"
euk_seqFile = outFile.split(".")[0] + "_euk.txt"

# gets the prokaryotes into an array
p = open(proFile, 'r')
proks = []
for line in p:
    for abr in line.split(' '):
        proks.append(abr)

# Open file to write to:
file_obj = open(outFile, "w")
file_obj2 = open(errorFile, "w")
file_obj3 = open(euk_seqFile, "w")
file_obj4 = open(prok_seqFile, "w")

# Link for the pfam
link = ('https://www.genome.jp/dbget-bin/get_linkdb?-t+9+pf:' + name)
page = requests.get(link)
print("Fetching from: " + link)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Gets the correct tag
table = soup.find_all("a")

# Iterates through all the <a> tags
iterTable = iter(table)
for b in iterTable:
    protein = b.text.strip()

    min_three = protein.split(':')[0]
    if min_three in proks:
        file_obj4.write(protein + "\n")
    else:
        file_obj3.write(protein + "\n")

file_obj.close()
file_obj2.close()
file_obj3.close()
file_obj4.close()
