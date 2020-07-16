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

print(type(g.getsdfG()))
nx.draw_networkx(g.getsdfG())
plt.show()

print('节点信息',g.getsdfG().nodes(data=True))
print('边信息',g.getsdfG().edges(data=True))

print(g.getVertexSize())

vset = g.getVerticesSet()
print(str(vset)+"vset")

vlist = g.getVerticesList()
print(vlist[1].getExeTimeOnMappedProcessor())

v = g.getVertexByID(0)
print(v.getName())

print(g.getName())
print('g.getDegreeofVertex(a):'+str(g.getDegreeofVertex(a)))

Ev = g.getEdgesofVertex(a)
for e in Ev:
    print(e.getName())

Ev = g.getIncomingEdges(a)
print(len(Ev))

Ev = g.getOutgoingEdges(a)
print(Ev == None)
for e in Ev:
    print('Outgoing::'+e.getName())

e = g.getIDofEdge(e2)
print(type(e))

ee = g.getEdgeofID(e)
print(ee.getName())

eID = g.getAllOutgoingEdgeID(0)
print(eID)

v = g.getVertexByname('a')
print(v.getName())

v = g.getTargetIDofEdge(e2)
print(v)

v = g.getAllIncomingVertexs(b)
for i in range(len(v)):
    print(v[i].getName())


e = g.getEdgebyVertex(c, b)
print(e)

subg = g.DirectedSubgraph()
print(subg.getsdfG().edges(data=True))
nx.draw_networkx(subg.getsdfG())
plt.show()
subg.getsdfG()['a']['b'][0]['name'] = 'eeee1'
print(subg.getsdfG()['a']['b'][0]['consumeRate'])