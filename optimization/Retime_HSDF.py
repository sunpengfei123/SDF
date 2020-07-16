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

    def getRetimedSDFG(self):
        self.__sdfG.Refresh()
        return  self.__sdfG

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
            print(self.__retime)
            self.retimedG = tr.retimeSDF(self.__retime)
            retime_CP = HSDF_CP.HSDF_CP(self.retimedG)
            cp = retime_CP.clockPeriod()

            for j in range(self.__sdfG.getVertexSize()):
                if retime_CP.pathTime[j] > c:
                    self.__retime[j] = self.__retime[j] +  1

        retime_CP = HSDF_CP.HSDF_CP(self.retimedG)
        cp = retime_CP.clockPeriod()
        print('cp: '+str(cp)+'  c: '+str(c))
        if cp > c:
            return False
        else:
            return True