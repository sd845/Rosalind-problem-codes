def insertion_sort(n, arr):

    swaps = 0

    for i in range(1,n):
        k = i
        while (k>0 and arr[k]<arr[k-1]):
            arr[k], arr[k-1] = arr[k-1], arr[k]
            swaps += 1
            k-=1

    return swaps, arr

with open('rosalind_ins.txt', 'r') as f:

    data = f.read()
    data = data.split("\n")
    n = int(data[0])
    data = data[1].split(" ")
    arr = [int(i) for i in data]

    swaps, sorted_arr = insertion_sort(n, arr)
    print(swaps)
