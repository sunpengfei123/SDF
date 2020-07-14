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

print('节点信息',g.getsdfG().nodes(data=True))
print('边信息',g.getsdfG().edges(data=True))

p = nx.dijkstra_path(g.getsdfG(), 'a', 'c', 'delay')


subg = g.getsdfG()
remove = []
num = 0
vv1 = -1
vv2 = -1
for v1, v2, info in g.getsdfG().edges(data=True):
    if v1 == vv1:
        if v2 == vv2:
            num = num + 1
    if info['delay'] != 0:
        print(v1,v2)
        print(info)
        remove.append([v1,v2,num])

    vv1 = v1
    vv2 = v2

print(remove)
subg.remove_edges_from(remove)
print(subg.edges(data=True))
nx.draw_networkx(subg)
plt.show()

# subg.remove_edge('a','c',0)
# print(subg.edges(data=True))