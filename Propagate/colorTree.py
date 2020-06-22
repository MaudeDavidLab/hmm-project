# Takes in a newick tree and outputs a phyloxml tree with all the branches colored 
#   either by KO or red for no_KO

import os
import sys
import random 

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny

def getRandomNum():
	for x in range(1):
		hold1=random.randint(0,255)
		hold2=random.randint(0,255)
		hold3=random.randint(0,255)
		return hold1, hold2, hold3

if len(sys.argv) != 3:
	# input tree needs to be in newick format
	print("Usage: python colorTree.py <inputTree> <outputFileName>")
	sys.exit()

inputTree=sys.argv[1]
outputTree=sys.argv[2]
outputTree+='.xml'

# loads a newick tree
tree=Phylo.read(inputTree, "newick")

kos=[]

for clade in tree.find_clades():
	if clade.is_terminal():
		if clade.name[-5:]=='no_KO':
			clade.color = Phylo.PhyloXML.BranchColor(255,0,0)
		else:
			if clade.name[-6:] not in kos:
				kos.append(clade.name[-6:])

rgbs=[]
i=0
while i < len(kos):
	rgbs.append(getRandomNum())
	i+=1

for clade in tree.find_clades():
	if clade.is_terminal():
		if clade.name[-5:]!='no_KO':
			index = (kos.index(clade.name[-6:]))
			rgb=(rgbs[index])
			clade.color = Phylo.PhyloXML.BranchColor(rgb[0],rgb[1],rgb[2])


# checks which branches still needs to be colored
#  prints out the names of that branch
print ('checking for branches that still need to be colored:')
x=0
for clade in tree.find_clades():
	if clade.name:
		if not (clade.color):
			print clade.name
			x=1
if x==0:
	print ('\n	all branches are colored')

Phylo.write(tree, outputTree, "phyloxml")
print ('\ncolored tree written to: '+ outputTree)

#Phylo.draw(tree)
