def two_way(arr, pivot):

    # initialize counters
    i = 1 # since pivot is at arr[0]
    j = len(arr)-1

    while i<j:

        while arr[i]<pivot and i<j:
            i+=1
        while arr[j]>pivot and i<j:
            j-=1

        arr[i], arr[j] = arr[j], arr[i]
        if j==i+1: break

    i = 0
    while arr[i+1]<pivot:i+=1
    arr[0], arr[i] = arr[i], arr[0]

    return arr

with open('rosalind_par.txt', 'r') as f:

    data = f.read().split("\n")
    n, arr = int(data[0]), data[1]
    arr = arr.split(" ")
    arr = [int(i) for i in arr]
    pivot = arr[0]
    arr = two_way(arr, pivot)
    for i in arr:
        print(i, end=" ")
