# Computing GC Content

from collections import Counter
import numpy as np

highest = 0
rosalind_id = ''

def calculate_gc_content(identifier, sequence):
    """ function to calculate GC content in a sequence"""
    
    global highest
    global rosalind_id
    
    counter = Counter(sequence)
    gc_content = round((counter['G']+counter['C'])/(sum(counter.values()))*100, 6)
    
    if gc_content > highest:
        highest = gc_content
        rosalind_id = identifier

with open('rosalind_gc.txt', 'r') as f:
    data = f.read()
    data = data.split(">")[1:]
    for fasta_seq in data:
        seq = fasta_seq.split("\n")
        identifier = seq[0]
        nt_sequence = ''.join(seq[1:])
        result = calculate_gc_content(identifier, nt_sequence)

print(rosalind_id)
print(highest)
