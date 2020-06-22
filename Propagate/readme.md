#### Does the Following within each of the 10 directories:
- Creates an initial colored tree  
- Propagates the sequences  
- Separates the colored branches into separate files  
- Aligns each of the KO files  
- Only keeps the files that contains at least 1 alignment  
- Build hmmprofiles for the aligned files  
- hmmpress each of the hmmprofiles  
- hmmsearch  
- Gets all the files with hits  
- Generates tables  

### Usage:
```
./pipe3 90percent.dnd 90percent.fasta original10.fasta finalDir
```
