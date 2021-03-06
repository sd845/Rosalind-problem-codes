from collections import defaultdict

def build_graph(edges):

    graph = defaultdict(list)

    for pair in edges:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])

    return graph

with open('rosalind_ddeg.txt', 'r') as f:

    data = f.read()
    # first line is number of edges and vertices
    # last line is empty
    data = data.split("\n")
    v,e = data[0].split(" ")
    data = data[1:-1]
    edges = []

    for pair in data:
        pair = pair.split(" ")
        edges.append([int(pair[0]), int(pair[1])])

    graph = build_graph(edges)


    for i in range(1,len(graph.keys())+1):
        neighbors = graph[i]
        deg_sum = 0

        for n in neighbors:
            deg_sum += len(graph[n])
        print(deg_sum, end=" ")

    k = len(graph)
    while k!=int(v):
        print(0, end=" ")
        k += 1
