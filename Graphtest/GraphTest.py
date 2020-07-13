import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import SDFgraph as SDFG
from sdfGraph import DefEdge as DE


g = SDFG.SDFgraph('test')

a = DV.Vertex('a',2)
g.addVertex(a)

b = DV.Vertex('b',3)
g.addVertex(b)

c = DV.Vertex('c',3)
g.addVertex(c)

e1 = DE.SDFedge('e1',2,2,2)
g.addEdge(a,b,e1)

e2 = DE.SDFedge('e2',1,1,1)
g.addEdge(a,c,e2)

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
print(g.getDegreeofVertex(a))

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