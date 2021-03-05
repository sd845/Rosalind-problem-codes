def find_substrings(s, t):
    """ find locations of substrings in a given strings"""

    indices = []
    for i in range(0,len(s)-len(t)+1):
        substr = s[i:i+len(t)]
        if substr==t:
            indices.append(i+1)
    return indices

with open('rosalind_subs.txt', 'r') as f:
    data = f.read()
    data = data.split("\n")
    result = find_substrings(data[0], data[1])
    print(' '.join([str(i) for i in result]))
