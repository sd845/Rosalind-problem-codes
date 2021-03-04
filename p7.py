# Mendel's First Law

def calculate_prob(k, m, n):
    """ calculates probability that two randomly selected 
    mating organisms will produce an individual possessing 
    a dominant allele"""
    
    # here k individuals are homozygous dominant for a factor, 
    # m are heterozygous, and 
    # n are homozygous recessive
    
    prob = [
        k*(k-1)*1, #AA and AA
        k*m*1, #AA and Aa
        k*n*1, #AA and aa
        m*k*1, #Aa and AA
        m*(m-1)*0.75, #Aa and Aa
        m*n*0.5, #Aa and aa
        n*k*1, #aa and AA
        n*m*0.5, #aa and Aa
        n*(n-1)*0, #aa and aa
    ]
    
    total = k+m+n
    return sum(prob)/(total*(total-1))

with open('rosalind_iprb.txt', 'r') as f:
    data = f.read()
    data = data.strip("\n")
    data = data.split(" ")
    result = calculate_prob(int(data[0]),int(data[1]),int(data[2]))
    print(result)
