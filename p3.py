def rev_complement(string):
    """ function to calculate the reverse complement of a DNA strand """
    
    complement_dict = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'T'
    }
    
    string = string.strip('\n')
    string = string[::-1]
    rev_comp = ''
    
    for i in string:
        rev_comp += complement_dict[i]
        
    return rev_comp

with open('rosalind_revc.txt', 'r') as f:
    data = f.read()
    result = rev_complement(data)
    print(result)
