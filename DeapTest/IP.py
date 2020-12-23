from SDFIO import xmlTosdfG
from z3 import *

class IP:
    def __init__(self, path):
        self.__path = path
        self.__t = xmlTosdfG.xmlTosdfG(self.__path)


    def getIP(self, h):


        g = self.__t.get_sdfG()

        # for v in g.getVerticesList():
        #     v.addNewProcessorType('arm1', math.ceil(v.getExeTimeOnMappedProcessor()/2))
        # print(v.getprocessorAndexetimeDict().get('arm1'))

        # print('节点信息', g.nodes())
        # print('边信息', g.edges())

        vNum = g.getVertexSize()
        eNum = g.getEdgeSize()

        # x = [1, 1, 1, 1, 1,
        #      0, 1, 1, 1, 1,
        #      0, 1, 1, 0, 1,
        #      0, 0, 1, 0, 1,
        #      1, 1, 1, 0, 1,
        #      1, 0, 1, 1, 1]
        x = h
        v = {}
        e = {}

        for vv in g.getVerticesList():
            v[g.getIDofVertex(vv)] = Int("v" + g.getIDofVertex(vv).__str__())
            # x[g.getIDofVertex(vv)] = Int('x' + g.getIDofVertex(vv).__str__())

        for ee in g.getEdgeList():
            e[g.getIDofEdge(ee)] = Int('e' + g.getIDofEdge(ee).__str__())

        w = Int('w')

        solver = Optimize()  # 创建一个求解器对象

        for i in range(vNum):
            solver.add(v[i] >= 0)
            solver.add(w >= v[i] + g.getVertexByID(i).getprocessorAndexetimeDict().
                       get(g.getVertexByID(i).getProcessorTypeNameArray()[x[i]]))
            for j in range(i + 1, vNum):
                if x[i] == x[j]:
                    solver.add(Or(v[i] >= v[j] + g.getVertexByID(j).getprocessorAndexetimeDict().
                                  get(g.getVertexByID(j).getProcessorTypeNameArray()[x[i]]),
                                  v[j] >= v[i] + g.getVertexByID(i).getprocessorAndexetimeDict().
                                  get(g.getVertexByID(i).getProcessorTypeNameArray()[x[i]])))

        for i in range(eNum):
            solver.add(e[i] >= 0)
            ee = g.getEdgeofID(i)
            vID = g.getSourceIDofEdge(g.getEdgeofID(i))
            # solver.add(e[i] >= v[vID] + g.getVertexByID(vID).getExeTimeOnMappedProcessor() * (1 - x[vID]) +
            #            math.ceil(g.getVertexByID(vID).getExeTimeOnMappedProcessor()/2) * x[vID])
            solver.add(e[i] >= v[vID] + g.getVertexByID(vID).getprocessorAndexetimeDict().
                       get(g.getVertexByID(vID).getProcessorTypeNameArray()[x[vID]]))

            vsIDi = g.getSourceIDofEdge(g.getEdgeofID(i))
            vtIDi = g.getTargetIDofEdge(g.getEdgeofID(i))

            solver.add(If(x[vsIDi] == x[vtIDi], w >= e[i], w >= e[i] + ee.gettranTime()))
            if g.getEdgeofID(i).getDelay() == 0:
                solver.add(If(x[vsIDi] != x[vtIDi], v[vtIDi] >= e[i] + ee.gettranTime(), v[vtIDi] >= e[i]))

            for j in range(i + 1, eNum):
                vsIDj = g.getSourceIDofEdge(g.getEdgeofID(j))
                vtIDj = g.getTargetIDofEdge(g.getEdgeofID(j))
                solver.add(If(And(x[vsIDi] != x[vtIDi], x[vsIDj] != x[vtIDj]),
                              Or(e[j] >= e[i] + 1, e[i] >= e[j] + 1), e[i] >= 0))

        solver.minimize(w)

        # print ("asserted constraints...")
        # for c in solver.assertions():
        #     print(c)

        # print("开始求解")
        if solver.check() == sat:  # check()方法用来判断是否有解，sat(satisify)表示满足有解
            ans = solver.model()  # model()方法得到解
            # print(ans[w])
        else:
            print("no ans!")

        return int(ans[w].as_string())
