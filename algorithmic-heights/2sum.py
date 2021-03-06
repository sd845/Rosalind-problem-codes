from collections import defaultdict

def two_sum(arr, k):

    dct = defaultdict()

    for i in range(len(arr)):
        if arr[i] in dct:
            return [dct[arr[i]]+1, i+1]
        else:
            dct[k-arr[i]] = i

    return -1


with open('rosalind_2sum.txt', 'r') as f:

    data = f.read()
    data = data.split("\n")
    data = data[:-1]

    n, length = data[0].split(' ')
    n, length = int(n), int(length)

    for arr in data[1:]:
        arr = arr.split(' ')
        arr = [int(i) for i in arr]

        # sum of two numbers must be zero
        s= 0

        result = two_sum(arr, s)
        if result == -1: print(result)
        else: print(*result)
