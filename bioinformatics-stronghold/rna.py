
#Transcribing DNA into RNA
def make_rna(string):
    """ function to transcribe DNA into RNA"""
    
    string = string.replace('T', 'U')
    return string

with open('rosalind_rna.txt', 'r') as f:
    data = f.read()
    result = make_rna(data)
    print(result)
