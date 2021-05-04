class SUM:
    def __init__(self):
        pass

    def two_sum(self, arr, target=0):
        tmp_dict = {}
        for i in range(len(arr)):
            if arr[i] in tmp_dict:
                return (tmp_dict[arr[i]]+1, i+1)
            else:
                tmp_dict[target-arr[i]] = i
        return -1

    def three_sum(self, arr):
        for i in range(len(arr)):
            target = -arr[i]
            result = self.two_sum(arr[i+1:], target)
            if result != -1:
                return (i+1, i+result[0]+1, i+result[1]+1)
        return -1

with open('rosalind_3sum.txt', 'r') as f:

    data = f.read().split("\n")
    input = data[1:-1]

    for arr in input:
        arr = arr.split(" ")
        arr = [int(i) for i in arr]

        obj = SUM()
        result = obj.three_sum(arr)

        if result == -1: print(result)
        else: print(*result)
