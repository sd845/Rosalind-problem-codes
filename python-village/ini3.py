import numpy as np

def print_words(s,slices):
    print(s[slices[0]:slices[1]+1], s[slices[2]:slices[3]+1])

if __name__ == "__main__":
    with open("rosalind_ini3.txt", "r") as f:
        data = f.read().split("\n")
        strings = data[0]
        slices = data[1].split(" ")
        slices = [int(i) for i in slices]
        print_words(strings, slices)
