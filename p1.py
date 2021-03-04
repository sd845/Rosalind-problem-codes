from collections import Counter

def count_nts(string):
    """ function to count DNA nucleotides """
    
    nt_dict = Counter(string)
    return ("{A} {C} {G} {T}".format(A=nt_dict['A'],G=nt_dict['G'],C=nt_dict['C'],T=nt_dict['T']))

with open('rosalind_dna.txt', 'r') as f:
    data = f.read()
    result = count_nts(data)
    print(result)
