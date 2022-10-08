
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Polygon
import numpy as np

G = nx.Graph()

colors = {0:"red", 1:"green", 2:"blue", 3:"yellow"}

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2), (1,3), (2,4), (3,5), (4,5)])

nodes = list(G.nodes)
edges = list(G.edges)

color_lists = []
color_of_edge = []
some_colors = ['red','green','blue','yellow']

for i in range(len(nodes) + 1):
    color_lists.append([])
    color_of_edge.append(-1)

def getSmallestColor(ls1,ls2):
    i = 1
    while(i in ls1 or i in ls2):
        i = i + 1
    return i

i = 0
for ed in edges:
    newColor = getSmallestColor(color_lists[ed[0]],color_lists[ed[1]])
    color_lists[ed[0]].append(newColor)
    color_lists[ed[1]].append(newColor)
    color_of_edge[i] = newColor
    i = i + 1

G = nx.Graph()

for i in range(len(edges)):
    G.add_edge(edges[i][0],edges[i][1],color=some_colors[color_of_edge[i]-1])

colors = nx.get_edge_attributes(G,'color').values()
nx.draw(G, edge_color=colors, with_labels=True, width=2)

plt.show()


#FACE COLOR

import networkx as nx

G = nx.Graph()

colors = {0:"red", 1:"green", 2:"blue", 3:"yellow"}

G.add_nodes_from([1,2,3,4,5, 6, 7])
G.add_edges_from([(1,2), (1,3), (2,4), (2,7), (3,4), (4,5), (4,6), (5,6), (5,7)])

nodes = list(G.nodes)
edges = list(G.edges)
some_colors = ['red','green','blue','yellow']

no_of_faces = len(edges)+2-len(nodes)-1
def regionColour(regions):
    print("NO OF FACES : "+str(regions))
    for i in range(1,regions+1):
        print("FACE ", i, ": "+some_colors[i%4])

regionColour(no_of_faces)


#VERTEX COLOR

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

colors = {0:"red", 1:"green", 2:"blue"}

G.add_nodes_from([1,2,3,4,5, 6, 7])
G.add_edges_from([(1,2), (1,3), (2,4), (2,7), (3,4), (4,5), (4,6), (5,6), (5,7)])

d = nx.coloring.greedy_color(G, strategy = "largest_first")
node_colors = []
for i in sorted (d.keys()):
    node_colors.append(colors[d[i]])

nx.draw(G, node_color = node_colors, with_labels = True, width = 5)

plt.show
