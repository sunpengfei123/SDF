from analysis import HSDF_CP as Hcp
import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE
from sdfGraph import SDFgraph as G

g = G.SDFgraph('g')

a = DV.Vertex('a', 2)
b = DV.Vertex('b', 3)
c = DV.Vertex('c', 2)
e1 = DE.SDFedge('e1', 0, 1, 2)
e2 = DE.SDFedge('e2', 2, 1, 1)
e3 = DE.SDFedge('e3', 1, 1, 1)
e4 = DE.SDFedge('e4', 0, 1, 1)
e5 = DE.SDFedge('e5', 0, 1, 1)


g.addVertex(a)
g.addVertex(b)
g.addVertex(c)
g.addEdge(a, b, e1)
g.addEdge(a, c, e2)
g.addEdge(b, c, e3)
# g.addEdge(b, c, e4)
# g.addEdge(b, c, e5)

nx.draw_networkx(g.getsdfG())
plt.show()

print('节点信息',g.nodes())
print('边信息',g.edges())

Hsdf_Cp = Hcp.HSDF_CP(g)
Hsdf_Cp.HSDF_WD()

print(Hsdf_Cp.getW())
print(Hsdf_Cp.getD())

p = Hsdf_Cp.clockPeriod()
print(Hsdf_Cp.pathTime)