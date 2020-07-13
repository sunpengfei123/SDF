import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from typing import List

G = nx.MultiDiGraph()

G.add_node('a',exeTimeOnMappedProcessor = 9 )

G.add_node('b',exeTimeOnMappedProcessor = 1 )
print(G.nodes(data=True))
G.add_edge('a','b',name = 'e1' ,consumeRate = 1, produceRate = 1)

print('图中所有的节点', G.nodes(data=True))
print('图中节点的个数', G.number_of_nodes())

print(G.edges(data=True))
print('图中所有的边', G.edges(data=True))
print('图中边的个数', G.number_of_edges())
for v1,v2,i in G.edges(data=True):
    print(i['name'])

print(G.number_of_edges())

nx.draw_networkx(G)
plt.show()


print("test1")

a = DV.Vertex('a', 2)
b = DV.Vertex('b', 3)
v = [DV.Vertex]
v.append(a)
v.append(b)
print(type(v))

