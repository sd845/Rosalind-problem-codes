def merge(n, m, arr1, arr2):

    arr = [0 for i in range(n+m)]
    i, j, k = 0, 0, 0

    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1

    while(i<n):
        arr[k]=arr1[i]
        k+=1
        i+=1

    while(j<m):
        arr[k]=arr2[j]
        k+=1
        j+=1

    return arr

with open('rosalind_mer.txt', 'r') as f:

    data = f.read()
    data = data.split("\n")
    data = data[:-1]

    n, arr1, m, arr2 = int(data[0]), data[1].split(" "), int(data[2]), data[3].split(" ")
    arr1 = [int(i) for i in arr1]
    arr2 = [int(j) for j in arr2]

    result = merge(n, m, arr1, arr2)
    print(*result)
