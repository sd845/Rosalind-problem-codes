import numpy as np

def find_sum(a,b):
    total = 0
    for i in range(a,b):
        if i%2!=0: total+=i
    return total

if __name__ == "__main__":
    with open("rosalind_ini4.txt", "r") as f:
        data = f.read().split("\n")[:-1]
        data = data[0].split(" ")
        a, b = int(data[0]), int(data[1])
        print(find_sum(a,b))
