from collections import defaultdict

class BFS:
    
    def build_graph(self, nodes):
        
        graph = defaultdict(list)
        
        for n1,n2 in nodes:
            graph[n1].append(n2)
            
        return graph
    
    
    def find_shortest_path(self, graph):
    
        queue = [1]
        visited = []
        
        min_dist = defaultdict(lambda:-1)
        min_dist[1] = 0
        
        while queue:
            current = queue.pop(0)
#             print(graph[current])
            for node in graph[current]:
                if node not in visited:
                    queue.append(node)
                    visited.append(node)
                    
                    min_dist[node] = min_dist[current] + 1
                    
                    
        min_dist[1] = 0
        return min_dist    
            
        
    def print_result(self, result, n):
        for i in range(1, n+1):
            print(result[i], end=" ")

with open('rosalind_bfs.txt', 'r') as f:
    
    bfs = BFS()
    
    data = f.read()
    data = data.split("\n")
    n = data[0].split(' ')
    n = int(n[0])
    data = data[1:-1]
    nodes_list = []
    
    for edge in data:
        nodes = edge.split(" ")
        nodes = [int(i) for i in nodes]
        nodes_list.append(nodes)
        
    graph = bfs.build_graph(nodes_list)
    result = bfs.find_shortest_path(graph)
    bfs.print_result(result, n)
        
