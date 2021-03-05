# Counting Point Mutations
def hamming_distance(sequence1, sequence2):
    """ function that calculates hamming distance between two DNA sequences"""
    
    hamming_score = 0
    
    for nt1,nt2 in zip(sequence1,sequence2):
        if nt1 != nt2: hamming_score +=1
            
    return hamming_score

with open('rosalind_hamm.txt', 'r') as f:
    data = f.read()
    data = data.split("\n")
    result = hamming_distance(data[0], data[1])
    print(result)
