# Rabbits and Recurrence Relations
def total_rabbits(n, k):
    """ function that claculates recurrence relations via dynamic programming """
    
    dp = dict({
        1:1,
        2:1,
    })
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + k*dp[i-2]
        
    return dp[n]

with open('rosalind_fib.txt', 'r') as f:
    data = f.read()
    data = data.strip("\n")
    data = data.split(" ")
    result = total_rabbits(int(data[0]), int(data[1]))
    print(result)
