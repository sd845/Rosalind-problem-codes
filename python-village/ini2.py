def find_hypotensue(a,b):
    return a**2 + b**2

if __name__ == "__main__":
    with open("rosalind_ini2.txt", "r") as f:
        data = f.read().split("\n")[:-1]
        data = data[0].split(" ")
        a, b = int(data[0]), int(data[1])
        print(a,b)
        print(find_hypotensue(a,b))
