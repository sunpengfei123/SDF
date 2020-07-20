import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import SDFgraph as SDFG
from sdfGraph import DefEdge as DE


g = SDFG.SDFgraph('test')

a = DV.Vertex('a', 2)
b = DV.Vertex('b', 3)
c = DV.Vertex('c', 2)
e1 = DE.SDFedge('e1', 0, 1, 2)
e2 = DE.SDFedge('e2', 1, 1, 1)
e3 = DE.SDFedge('e3', 1, 1, 1)
e4 = DE.SDFedge('e4', 0, 1, 1)
e5 = DE.SDFedge('e5', 0, 1, 1)

g.addVertex(a)
g.addVertex(b)
g.addVertex(c)
g.addEdge(a, b, e1)
g.addEdge(a, c, e2)
g.addEdge(b, c, e3)
g.addEdge(b, c, e4)
g.addEdge(b, c, e5)

nx.draw_networkx(g.getsdfG())
plt.show()

print('节点信息',g.nodes())
print('边信息',g.edges())

print(g.getVertexSize())
