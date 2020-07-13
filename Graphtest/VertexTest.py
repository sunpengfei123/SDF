from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE
v1 = DV.Vertex('a',1)
print(v1.name)

e1 = DE.SDFedge('e1',3,2,4)

e = []
e.append(e1)

print(e[0].delay)
