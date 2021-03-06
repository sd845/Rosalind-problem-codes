def binary_search(arr, element):
    """ function that performs binary search"""

    beg = 0
    last = len(arr)

    while beg <= last:

        mid = (beg + last)//2

        if arr[mid]>element:
            last = mid-1
        elif arr[mid]<element:
            beg = mid+1
        else:
            return mid+1

    return -1


with open('rosalind_bins.txt', 'r') as f:

    data = f.read()
    data = data.split("\n")
    arr, elements = data[2], data[3]
    arr, elements = arr.split(" "), elements.split(" ")
    arr, elements = [int(i) for i in arr], [int(i) for i in elements]

    indices = []

    for element in elements:
        indices.append(binary_search(arr, element))

    print(*indices)
