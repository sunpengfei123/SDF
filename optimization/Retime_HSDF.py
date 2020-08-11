from sdfGraph import SDFgraph
from sdfGraph import SDFTop
from analysis import HSDF_CP
from sdfGraph import SDFTransform

class Retime_HSDF:
    def __init__(self, g: SDFgraph.SDFgraph):
        gg = g.copySDFG()
        self.__sdfG = gg
        self.__MinCP = -1
        self.__data =HSDF_CP.HSDF_CP(g)
        self.__retime = []

    def getCP(self):
        return self.__data.clockPeriod()

    def getMinCP(self):
        return self.__MinCP

    def getRetimedSDFG(self):
        # self.__sdfG.Refresh()
        return  self.retimedG

    # self.retimedG
    def getRetime(self):
        return self.__retime

    # Algorithm FEAS
    def feasibleCPTest_2(self, c: int):
        # 初始化重定时向量
        for i in range(self.__sdfG.getVertexSize()):
            self.__retime.append(0)

        retimedG = SDFgraph.SDFgraph('Retimed_'+str(self.__sdfG.getName()))
        tr = SDFTransform.SDFTransform(self.__sdfG)

        cp = 0
        for i in range(self.__sdfG.getVertexSize() - 1):
            # print(self.__retime)
            self.retimedG = tr.retimeSDF(self.__retime)
            retime_CP = HSDF_CP.HSDF_CP(self.retimedG)
            cp = retime_CP.clockPeriod()

            for j in range(self.__sdfG.getVertexSize()):
                if retime_CP.pathTime[j] > c:
                    self.__retime[j] = self.__retime[j] +  1

        self.retimedG = tr.retimeSDF(self.__retime)
        retime_CP = HSDF_CP.HSDF_CP(self.retimedG)
        cp = retime_CP.clockPeriod()
        # print('cp: '+str(cp)+'  c: '+str(c))
        if cp > c:
            return False
        else:
            return True

    def minCP(self):
        Max = self.__data.clockPeriod()
        Min = -1
        for v in self.__sdfG.getVerticesList():
            if Min < v.getExeTimeOnMappedProcessor():
                Min = v.getExeTimeOnMappedProcessor()

        mid = Max

        while Min <= Max:

            mid = int((Max + Min)/2)
            #print([Max, Min, mid])
            isFeasible = self.feasibleCPTest_2(mid)

            if not (isFeasible):
                # print(str(mid)+" is not a feasible clock period. Check a larger one.")
                Min = mid + 1
                mid = Min
            else:
                # print(str(mid) + " is a feasible clock period. Check a smaller one.")
                Max = mid - 1

        # print(str(mid) + " is a minimal clock period. ")
        self.__MinCP = mid