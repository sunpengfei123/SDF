from sdfGraph import SDFTop

import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import SDFgraph as SDFG
from sdfGraph import DefEdge as DE

g = SDFG.SDFgraph('test')

a = DV.Vertex('a', 2)
g.addVertex(a)

b = DV.Vertex('b', 3)
g.addVertex(b)

c = DV.Vertex('c', 3)
g.addVertex(c)

e1 = DE.SDFedge('e1', 2, 1, 2)
print(e1.getConsumeRate())
print(e1.getProduceRate())
g.addEdge(a, b, e1)

e2 = DE.SDFedge('e2', 1, 1, 1)
g.addEdge(a, c, e2)

print(type(g.getsdfG()))
nx.draw_networkx(g.getsdfG())
plt.show()

ev = g.getEdgeList()
print(ev[0])
gTop = SDFTop.SDFTop(g)
Cv = gTop.getConsVector()
print(Cv)

t = gTop.getRepVector()
print(t)