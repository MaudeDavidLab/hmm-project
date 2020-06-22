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
