from SDFIO import xmlTosdfG
from z3 import *
import math

# 测试图的文件夹目录
filedir = 'C:\\Study\\TestCase\\2016-TCAD\\d0\\a20q5k'
resultpath = "C:\\Study\\TestCase\\Z3Test\\2016\\d0\\a20q5k"

file_name = []


def getfile(path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称

    for file in files:  # 遍历文件夹
        if not os.path.isdir(path+'\\'+file):  # 判断是否是文件夹，不是文件夹才打开
            file_mess = os.path.splitext(file)
            filename, type = file_mess
            if type == '.xml':
                file_name.append(filename)
        else:
            getfile(path+'\\'+file)


getfile(filedir)
# print(file_name)


def Z3_optimize(path, filename):
    t = xmlTosdfG.xmlTosdfG(path+'\\'+filename+".xml")

    g = t.get_sdfG()
    # print('节点信息', g.nodes())
    # print('边信息', g.edges())

    vNum = g.getVertexSize()
    eNum = g.getEdgeSize()

    x = {}
    v = {}
    e = {}

    for vv in g.getVerticesList():
        v[g.getIDofVertex(vv)] = Int("v" + g.getIDofVertex(vv).__str__())
        x[g.getIDofVertex(vv)] = Int('x' + g.getIDofVertex(vv).__str__())

    for ee in g.getEdgeList():
        e[g.getIDofEdge(ee)] = Int('e' + g.getIDofEdge(ee).__str__())

    w = Int('w')

    solver = Optimize()  # 创建一个求解器对象

    for i in range(vNum):
        solver.add(v[i] >= 0)
        solver.add(x[i] >= 0)
        solver.add(x[i] <= 1)
        for j in range(i + 1, vNum):
            solver.add(
                If(And(x[i] == x[j], x[i] == 0), Or(v[i] >= v[j] + g.getVertexByID(j).getExeTimeOnMappedProcessor(),
                                                    v[j] >= v[i] + g.getVertexByID(i).getExeTimeOnMappedProcessor()),
                   v[i] >= 0))
            solver.add(If(And(x[i] == x[j], x[i] == 1),
                          Or(v[i] >= v[j] + math.ceil(g.getVertexByID(j).getExeTimeOnMappedProcessor() / 2),
                             v[j] >= v[i] + math.ceil(g.getVertexByID(i).getExeTimeOnMappedProcessor() / 2)),
                          v[i] >= 0))

    for i in range(eNum):
        solver.add(e[i] >= 0)
        vID = g.getSourceIDofEdge(g.getEdgeofID(i))
        # solver.add(e[i] >= v[vID] + g.getVertexByID(vID).getExeTimeOnMappedProcessor() * (1 - x[vID]) +
        #            math.ceil(g.getVertexByID(vID).getExeTimeOnMappedProcessor()/2) * x[vID])
        solver.add(
            If((x[vID] == 1), (e[i] >= v[vID] + math.ceil(g.getVertexByID(vID).getExeTimeOnMappedProcessor() / 2)),
               (e[i] >= v[vID] + g.getVertexByID(vID).getExeTimeOnMappedProcessor())))

        vsIDi = g.getSourceIDofEdge(g.getEdgeofID(i))
        vtIDi = g.getTargetIDofEdge(g.getEdgeofID(i))

        solver.add(If(x[vsIDi] == x[vtIDi], w >= e[i], w >= e[i] + 1))
        if g.getEdgeofID(i).getDelay() == 0:
            solver.add(If(x[vsIDi] != x[vtIDi], v[vtIDi] >= e[i] + 1, v[vtIDi] >= e[i]))

        for j in range(i + 1, eNum):
            vsIDj = g.getSourceIDofEdge(g.getEdgeofID(j))
            vtIDj = g.getTargetIDofEdge(g.getEdgeofID(j))
            solver.add(If(And(x[vsIDi] != x[vtIDi], x[vsIDj] != x[vtIDj]),
                          Or(e[j] >= e[i] + 1, e[i] >= e[j] + 1), e[i] >= 0))

    solver.minimize(w)

    # print ("asserted constraints...")
    # for c in solver.assertions():
    #     print (c)

    print("开始求解")
    if solver.check() == sat:  # check()方法用来判断是否有解，sat(satisify)表示满足有解
        ans = solver.model()  # model()方法得到解
        print(filename)
        print(ans[w])
        with open(resultpath+"\\"+filename+".txt", "w") as f:
            f.write(ans[w].__str__())
            f.write("\r\n")
            f.write(ans.__str__())
    else:
        print("no ans!")


for name in file_name:
    Z3_optimize(filedir, name)