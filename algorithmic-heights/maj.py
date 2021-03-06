from collections import Counter

def major_element(data):
    result = []

    for arr in data:
        arr = arr.split(" ")
        arr = [int(i) for i in arr]
        counter = Counter(arr)
        found = 0

        for key,value in counter.items():
            if value > n/2:
                result.append(key)
                found = 1
        if found == 0: result.append(-1)

    return result

with open('rosalind_maj.txt', 'r') as f:

    data = f.read()
    data = data.split("\n")
    k,n = data[0].split(" ")
    k,n = int(k), int(n)
    data = data[1:-1]
    result = major_element(data)
    print(*result)
