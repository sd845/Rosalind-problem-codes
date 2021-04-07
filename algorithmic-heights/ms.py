def merge_sort(arr):
    if len(arr)>1:
        n = len(arr)//2
        L = arr[:n]
        R = arr[n:]
        L = merge_sort(L)
        R = merge_sort(R)
        i, j, k = 0, 0, 0

        while(i<len(L) and j<len(R)):
            if L[i]<R[j]:
                arr[k]=L[i]
                k+=1
                i+=1
            else:
                arr[k]=R[j]
                j+=1
                k+=1

        while(i<len(L)):
            arr[k]=L[i]
            k+=1
            i+=1

        while(j<len(R)):
            arr[k]=R[j]
            j+=1
            k+=1

    return arr

with open('rosalind_ms.txt', 'r') as f:

    data = f.read().split("\n")
    n, arr = int(data[0]), data[1]
    arr = arr.split(" ")
    arr = [int(i) for i in arr]
    merge_sort(arr)

    for i in arr:
        print(i, end=" ")
