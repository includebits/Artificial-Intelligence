from queue import PriorityQueue 
import matplotlib.pyplot as plt 
import networkx as nx 
def best_first_search(source, target, n): 
    visited = [0] * n 
    visited[source] = True 
    pq = PriorityQueue() 
    pq.put((0, source)) 
    while pq.empty() == False: 
        u = pq.get()[1] 
        print(u, end=" ")
        if u == target: 
            break 
        for v, c in graph[u]: 
            if visited[v] == False: 
                visited[v] = True 
                pq.put((c, v)) 
        print() 
def addedge(x, y, cost): 
    graph[x].append((y, cost)) 
    graph[y].append((x, cost)) 
G = nx.Graph() 
v = int(input("Enter the number of nodes: ")) 
graph = [[] for i in range(v)]
e = int(input("Enter the number of edges: ")) 
print("Enter the edges along with  weights:") 
for i in range(e): 
    x, y, z = list(map(int, input().split())) 
    addedge(x, y, z)
    G.add_edge(x, y, weight = z) 
source = int(input("Enter the Source Node: ")) 
target = int(input("Enter the Target/Destination Node: ")) 
print("\nPath: ", end = "") 
best_first_search(source, target, v) 
