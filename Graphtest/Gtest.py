import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE
from sdfGraph import SDFgraph as SDFG

a = DV.Vertex('a', 1)
b = DV.Vertex('b', 2)
c = DV.Vertex('c', 3)
d = DV.Vertex('d', 4)

e1 = DE.SDFedge('e1', 1, 1, 1)
e2 = DE.SDFedge('e2', 1, 1, 1)
e3 = DE.SDFedge('e3', 0, 1, 1)
e4 = DE.SDFedge('e4', 0, 1, 1)

g = nx.MultiDiGraph()
g.add_node(a)
g.add_node(b)
g.add_edge(a, b, edge=e1)
nx.draw_networkx(g)
plt.show()
vv=[]
for v in g.nodes():
    vv.append(v)
    print(v.getName())
    print(v.getExeTimeOnMappedProcessor())

for v1, v2, e in g.edges(data=True):
    print(e['edge'].getName())


for vvv in vv:
    print(vvv.getName())


a.setName('aaa')
e1.setName('e1111')

for v in g.nodes():
    print(v.getName())
    print(v.getExeTimeOnMappedProcessor())

for v1, v2, e in g.edges(data=True):
    print(e['edge'].getName())

for vvv in vv:
    print(vvv.getName())