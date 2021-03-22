from collections import defaultdict

class DFS:

    def __init__(self):
        pass

    def build_graph(self, vertices):
        graph = defaultdict(list)
        for pair in vertices:
            nodes = pair.split(" ")
            n1, n2 = int(nodes[0]), int(nodes[1])
            graph[n1].append(n2)
            graph[n2].append(n1)
        return graph

    def find_connected_components(self, graph):
        remaining = set(graph.keys())
        counter = 0

        while remaining:
            visited = set()
            lst = [list(remaining)[0]]
            while lst:
                node = lst.pop()
                connected = graph[node]
                for n in connected:
                    if n not in visited:
                        lst.append(n)
                        visited.add(n)

            remaining = remaining - visited
            counter += 1

        return counter

with open('rosalind_cc.txt', 'r') as f:
    data = f.read()
    data = data.split("\n")
    nodes, edges = data[0].split(" ")
    nodes, edges = int(nodes), int(edges)
    data = data[1:-1]

    dfs = DFS()
    print(data)
    graph = dfs.build_graph(data)

    n = dfs.find_connected_components(graph)
    extras = set(range(1,nodes)) - set(graph.keys())
    print(n + len(extras))
