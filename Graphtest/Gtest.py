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

g = SDFG.SDFgraph('Retime_Hsdf_Test')
g.addVertex(a)
g.addVertex(b)
g.addVertex(c)
g.addVertex(d)

g.addEdge(c, a, e1)
g.addEdge(a, b, e2)
g.addEdge(c, d, e3)
g.addEdge(d, b, e4)

nx.draw_networkx(g.getsdfG())
plt.show()


print('节点信息',g.getsdfG().nodes(data=True))
print('边信息',g.getsdfG().edges(data=True))
ee = []
ee.append(e1)
ee.append(e3)
ee.append(e2)
ee.append(e4)


def take(elem):
    return elem.getName()


ee.sort(key=take)
for e in ee:
    print(e.getName())

# ee = g.getIncomingEdges(a)
# print(len(ee))
# for e in ee:
#     print(e.getName())