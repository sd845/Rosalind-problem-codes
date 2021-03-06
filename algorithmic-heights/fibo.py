def fibonacci(n):

    dct = {
        1:1,
        2:1,
    }
    for i in range(3,n+1):
        dct[i] = dct[i-1] + dct[i-2]

    return dct[n]

with open('rosalind_fibo.txt', 'r') as f:

    data = f.read()
    result = fibonacci(int(data))
    print(result)
