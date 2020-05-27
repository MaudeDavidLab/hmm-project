#### Formats the seuqences retrieved so that:
- End of sequence say 'no_KO' if sequence does not have a KO annotation
- End of sequence say 'KO_\<KO>' if sequence contains a KO annotation
- Trims the sequence name of the description to make easier to work with  

### Usage:
```
python format.py <inputFile> <outputFile>

# Example Usage:
python format.py tpr_3 tpr3_formatted
```
