import sys
from Bio import Phylo
from ete3 import Phyloxml

if len(sys.argv) != 3:
	print 'usage: python propogate.py inputXMLfile outputXMLfile'
	exit(1)
inputFile = sys.argv[1]
outputFile = sys.argv[2]

phyloTree = Phylo.read(inputFile,'phyloxml')

project = Phyloxml()
project.build_from_file(inputFile)
for eTree in project.get_phylogeny():
    eteTree=eTree
    
# creates a dictionary of [leafName, red, green, blue, branch length]
leafDict = {}
key=0
for clade in phyloTree.find_clades():
    if clade.is_terminal():
        cladeArr = []
        cladeArr.append(clade.name)
        x=clade.find_clades.im_self.color
        cladeArr.append(x.red)
        cladeArr.append(x.green)
        cladeArr.append(x.blue)
        cladeArr.append(clade.branch_length)
        leafDict.update({key:cladeArr})
        key += 1
        
def get_key(val): 
    for key, value in leafDict.items(): 
        if value[0]==val:
            toReturn = key
            break
    return toReturn

def updateArr(key1, key2):
    if 'no_KO' in leafDict.get(key1)[0]:
        known_arr = leafDict.get(key2)[:]
        change_arr = leafDict.get(key1)[:]
        changeKey = key1
        originalName = leafDict.get(key1)[0]
    else: 
        change_arr = leafDict.get(key2)[:]
        known_arr = leafDict.get(key1)[:]
        changeKey = key2
        originalName = leafDict.get(key2)[0]

    change_name = change_arr[0][:]
    change_name = change_name[:-5]
    change_name += 'P'
    change_index = known_arr[0].find('_K')
    change_KO = known_arr[0][change_index:]
    change_name += change_KO
    change_arr[0]=change_name
    change_arr[1]=known_arr[1]
    change_arr[2]=known_arr[2]
    change_arr[3]=known_arr[3]
    leafDict[changeKey] = change_arr
    l = eteTree.get_leaves_by_name(originalName)[0]
    l.name = change_name
    print 'propogated new, from', change_arr, known_arr

def isSame(arr):
    return all(x == arr[0] for x in arr)

def checkCond(arr):
    # check 'no_KO' in array
    first_cond = False
    # check 'no_KO' not in array
    second_cond = False
    # check every element has same KO
    third_cond_KO = []
    for leaf in arr: 
        if 'no_KO' in leaf:
            first_cond = True
        if 'no_KO' not in leaf:
            second_cond = True
            third_cond_KO.append(leaf[-6:])
    if first_cond == True and second_cond == True and isSame(third_cond_KO)==True: 
        toReturn = True
    else: 
        toReturn = False 
    return toReturn

propogating = 1
while propogating == 1:
    propogating = 0
    # goes through every leaf in leafDict
    for i in range(0,len(leafDict)):
        # gets its associated node 
        leaf = eteTree.get_leaves_by_name(leafDict.get(i)[0])[0]
        parent = leaf.up
        node = []
        for leaf in parent:
            node.append(leaf.name)   

        # checks if node is propogatable 
        if checkCond(node)==True:
            # split into known and unknown
            known = {}
            unknown = {}
            for leaf in node:
                key = get_key(leaf)
                if 'no_KO' in leaf:
                    unknown.update({key:leafDict.get(key)})
                else: 
                    known.update({key:leafDict.get(key)})
            # if unknown is shorter than any node, propogate 
            for leaf in unknown:
                shorter = False
                for knownLeaf in known: 
                    if unknown.get(leaf)[4] < known.get(knownLeaf)[4]:
                        propogating = 1
                        updateArr(leaf,knownLeaf)
                        break
# recolors the tree 
k=0
for clade in phyloTree.find_clades():
    if clade.is_terminal():
        ele=leafDict.get(k)
        if clade.name!=ele[0]:
            clade.color=Phylo.PhyloXML.BranchColor(ele[1],ele[2],ele[3])
            clade.name=ele[0]
        k+=1

#print leafDict

Phylo.write(phyloTree, outputFile, "phyloxml")
"""
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 20), dpi=100)
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(phyloTree, axes=axes)
fig.savefig('temp.png', dpi=fig.dpi)
"""
