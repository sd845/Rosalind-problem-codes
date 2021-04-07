class Heap:

    def __init__(self):
        pass

    def build_heap(self, arr, n):

        last_non_leaf_idx = (n//2) - 1
        for i in range(last_non_leaf_idx, -1, -1):
            self.heapify(arr, n, i)

        return arr

    def heapify(self, arr, n, i):

        largest = i
        left_child, right_child = (2*i)+1, (2*i)+2

        # to build a max heap
        if  left_child<n and arr[left_child]>arr[largest]: largest = left_child
        if  right_child<n and arr[right_child]>arr[largest]: largest = right_child

        if largest!=i:
            # swap positions and call heapify on sub tree
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)

    def print_heap(self, arr):
        for i in arr:
            print(i, end=" ")

with open('rosalind_hea.txt', 'r') as f:

    data = f.read().split("\n")
    n, arr = int(data[0]), data[1]
    arr = arr.split(" ")
    arr = [int(i) for i in arr]

    heap = Heap()
    max_heap = heap.build_heap(arr, n)
    heap.print_heap(max_heap)
