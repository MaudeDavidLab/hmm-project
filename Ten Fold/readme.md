#### Divides out the set of sequences across ten different folders  

### Usage:
```
./pipe2 <inputFile> <10% number>

# Example Usage:
# The total amount of sequences was 21,540, so 2,154 is 10%
./pipe2 tpr_formatted.fasta 2154
```

##### Pipeline Summary
- Grabs 10% Random Unique Sequences  
- Grabs the remaining 90%  
- Repeats this 9 more times (Gets the whole 10% -> 100%)  

##### Output: 10 directories that contain:
- 10percent.fasta  
- original10.fasta  
- 90percent.fasta  
