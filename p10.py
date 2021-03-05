import os
import numpy as np

def count_score(sequence):
    
    for i,nt in enumerate(sequence):
        nt_dict[nt][i] +=1
            
first = 0

with open('rosalind_cons.txt', 'r') as f:
    
    data = f.read()
    data = data.split(">")[1:]
    
    for fasta_seq in data:
        
        seq = fasta_seq.split("\n")
        identifier = seq[0]
        nt_sequence = ''.join(seq[1:])
        n = len(nt_sequence)

        if first == 0:

            # initialize dict to store information
            nt_dict = {'A': np.zeros(n),'C': np.zeros(n), 'G': np.zeros(n),'T': np.zeros(n),}
            count_score(nt_sequence)
            first = 1
            
        else:
            count_score(nt_sequence)
        
# print results
output = ''
for i in range(n):
    maximum = max([nt_dict[k][i] for k in nt_dict]).astype(int)
    ancestor = [k for k in nt_dict if nt_dict[k][i]==maximum][0]
    output += ancestor
print(output)
    
for k,v in nt_dict.items():
    print(f'{k}:'.format(k=k), *v.astype(int))
