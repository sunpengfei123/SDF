from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE
from sdfGraph import SDFgraph as SDFG
from analysis import HSDF_CP as Hcp
from optimization import Retime_HSDF as Retime
from  sdfGraph import SDFTransform as Tran

import networkx as nx
import matplotlib.pyplot as plt

a = DV.Vertex('a', 1)
b = DV.Vertex('b', 2)
c = DV.Vertex('c', 3)

e1 = DE.SDFedge('e1', 1, 1, 1)
e2 = DE.SDFedge('e2', 0, 1, 1)
e3 = DE.SDFedge('e3', 1, 1, 1)

# e1 = DE.SDFedge('e1', 0, 1, 1)
# e2 = DE.SDFedge('e2', 0, 1, 1)
# e3 = DE.SDFedge('e3', 1, 1, 1)

g = SDFG.SDFgraph('Retime_Hsdf_Test')
g.addVertex(a)
g.addVertex(b)
g.addVertex(c)

g.addEdge(a, b, e1)
g.addEdge(b, c, e2)
g.addEdge(c, a, e3)

nx.draw_networkx(g.getsdfG())
plt.show()


_CP = Hcp.HSDF_CP(g)

cp = _CP.clockPeriod()
print(_CP.pathTime)
print(cp)

print('节点信息',g.getsdfG().nodes(data=True))
print('边信息',g.getsdfG().edges(data=True))

Re = Retime.Retime_HSDF(g)
print(Re.feasibleCPTest_2(3))
print(Re.getRetime())
# tr = Tran.SDFTransform(g)
#
# Rg = tr.retimeSDF([0,1,0,1])
Rg = Re.getRetimedSDFG()
_NewCP = Hcp.HSDF_CP(Rg)
newcp = _NewCP.clockPeriod()
print(_NewCP.pathTime)
print(newcp)

print('R节点信息',Rg.getsdfG().nodes(data=True))
print('R边信息',Rg.getsdfG().edges(data=True))


