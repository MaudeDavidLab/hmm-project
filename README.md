# HMM Project Pipeline

## 1 Retrieve Sequences
Files stored within [Sequence Retrieval](https://github.com/MaudeDavidLab/hmm-project/tree/master/Sequence%20Retrieval)  

## 2 Format Sequences
Files stored within [Format Sequences](https://github.com/MaudeDavidLab/hmm-project/tree/master/Format%20Sequences)

## 3 Divide Across Ten Fold  
Files stored within [Ten Fold](https://github.com/MaudeDavidLab/hmm-project/tree/master/Ten%20Fold)

## 4 Align the 90percent sequences across each fold  
Using the Command (clustalo executable included in repo):
```
SGE_Batch -c 'clustalo -i 90percent.fasta --guidetree-out=90percent.dnd --threads=30 --outfile=90percentalign -v' -r outLog
```

## 5 Color Tree, Propagate, etc.
Files stored within [Propagate](https://github.com/MaudeDavidLab/hmm-project/tree/master/Propagate)

## 6 Get a Master Results table
Combine all the results from the 10 directories.  
- Remove the headers

## 7 Split Master Results table based on KO
Files stored within [Split](https://github.com/MaudeDavidLab/hmm-project/tree/master/Split)

## 8 Remove the unannotated Sequences  
Files stored within [Remove Unannotated](https://github.com/MaudeDavidLab/hmm-project/tree/master/Remove%20Unannotated)
