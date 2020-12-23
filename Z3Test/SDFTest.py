from SDFIO import xmlTosdfG
from z3 import *
import math
import time


#path = "C:\\Study\\TestCase\\2016-TCAD\\d0\\a10q1k"
path = "C:\\Study\\TestCase\\2020_MEC\\Test1_Muti_Pro\\a5"

filename = '0000.xml'#a20q1k-005


t = xmlTosdfG.xmlTosdfG(path+'\\'+filename)

g = t.get_sdfG()

# for v in g.getVerticesList():
#     v.addNewProcessorType('arm1', math.ceil(v.getExeTimeOnMappedProcessor()/2))

print('节点信息', g.nodes())
print('边信息', g.edges())

vNum = g.getVertexSize()
eNum = g.getEdgeSize()

x = {}
v = {}
e = {}

for vv in g.getVerticesList():
    v[g.getIDofVertex(vv)] = Int("v" + g.getIDofVertex(vv).__str__())
    x[g.getIDofVertex(vv)] = Int('x' + g.getIDofVertex(vv).__str__())

for ee in g.getEdgeList():
    e[g.getIDofEdge(ee)] = Int('e'+g.getIDofEdge(ee).__str__())

w = Int('w')

solver = Optimize()#创建一个求解器对象

for i in range(vNum):
    solver.add(v[i] >= 0)
    solver.add(x[i] >= 0)
    vi = g.getVertexByID(i)
    proNum = vi.getProcessorTypeNameArray().__len__()
    solver.add(x[i] < proNum)
    for pro in range(proNum):
        solver.add(If(x[i] == pro, w >= v[i] + vi.getprocessorAndexetimeDict().get(vi.getProcessorTypeNameArray()[pro]),
                      w >= 0))
    for j in range(i+1, vNum):
        for pro in range(proNum):
            # print(g.getVertexByID(j).getprocessorAndexetimeDict())
            # print(g.getVertexByID(j).getProcessorTypeNameArray()[pro])
            solver.add(If(And(x[i] == x[j], x[i] == pro),
                          Or(v[i] >= v[j] + g.getVertexByID(j).getprocessorAndexetimeDict().
                             get(g.getVertexByID(j).getProcessorTypeNameArray()[pro]),
                             v[j] >= v[i] + vi.getprocessorAndexetimeDict().get(vi.getProcessorTypeNameArray()[pro])),
                          v[i] >= 0))


for i in range(eNum):
    solver.add(e[i] >= 0)
    vID = g.getSourceIDofEdge(g.getEdgeofID(i))
    # solver.add(e[i] >= v[vID] + g.getVertexByID(vID).getExeTimeOnMappedProcessor() * (1 - x[vID]) +
    #            math.ceil(g.getVertexByID(vID).getExeTimeOnMappedProcessor()/2) * x[vID])
    vi = g.getVertexByID(vID)
    proNum = vi.getProcessorTypeNameArray().__len__()
    for pro in range(proNum):
        solver.add(If((x[vID] == pro), (e[i] >= v[vID] + vi.getprocessorAndexetimeDict().get(vi.getProcessorTypeNameArray()[pro])), (e[i] >= v[vID])))

    vsIDi = g.getSourceIDofEdge(g.getEdgeofID(i))
    vtIDi = g.getTargetIDofEdge(g.getEdgeofID(i))
    ei = g.getEdgeofID(i)
    solver.add(If(x[vsIDi] == x[vtIDi], w >= e[i], w >= e[i] + ei.gettranTime()))
    if ei.getDelay() == 0 :
        solver.add(If(x[vsIDi] != x[vtIDi], v[vtIDi] >= e[i] + ei.gettranTime(), v[vtIDi] >= e[i]))

    for j in range(i+1, eNum):
        vsIDj = g.getSourceIDofEdge(g.getEdgeofID(j))
        vtIDj = g.getTargetIDofEdge(g.getEdgeofID(j))
        solver.add(If(And(x[vsIDi] != x[vtIDi], x[vsIDj] != x[vtIDj]),
                      Or(e[j] >= e[i] + ei.gettranTime(), e[i] >= e[j] + g.getEdgeofID(j).gettranTime()), e[i] >= 0))

solver.minimize(w)

# print ("asserted constraints...")
# for c in solver.assertions():
#     print (c)

print("开始求解")
start = time.time()
if solver.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = solver.model() #model()方法得到解
    print(ans)
else:
    print("no ans!")

end = time.time()
print(end - start)