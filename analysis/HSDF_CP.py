import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import SDFgraph as SDFG
from sdfGraph import DefEdge as DE
from sdfGraph import SDFTop as Top

class HSDF_CP:
    def __init__(self, g: SDFG.SDFgraph):
        self.G = g
        self.__W = []
        self.__D = []
        self.dijkstra = []
        self.pathTime = []

    def getW(self):
        return self.__W

    def getD(self):
        return self.__D

    def HSDF_WD(self):
        N = self.G.getVertexSize()

        # 初始化W和D
        for i in range(N):
            self.dijkstra.append([])
            self.__W.append([])
            self.__D.append([])
            for j in range(N):
                self.dijkstra[i].append([])
                self.__W[i].append([])
                self.__D[i].append([])

        for i in range(self.G.getVertexSize()):
            for j in range(self.G.getVertexSize()):
                if i != j:
                    try:
                        self.dijkstra[i][j] = nx.dijkstra_path(self.G.getsdfG(), self.G.getVertexByID(i).getName(), self.G.getVertexByID(j).getName(), 'delay')
                        self.__W[i][j] = nx.dijkstra_path_length(self.G.getsdfG(), self.G.getVertexByID(i).getName(), self.G.getVertexByID(j).getName(), 'delay')
                        path = nx.dijkstra_path(self.G.getsdfG(), self.G.getVertexByID(i).getName(),
                                                self.G.getVertexByID(j).getName(), 'delay')
                        d = 0
                        for v in path:
                            d = d + self.G.getVertexByname(v).getExeTimeOnMappedProcessor()
                        self.__D[i][j] = d
                    except:

                        self.dijkstra[i][j] = -1
                        self.__W[i][j] = -1
                        self.__D[i][j] = -1
                else:
                    self.dijkstra[i][j] = self.G.getVertexByID(i)
                    self.__W[i][j] = -1
                    self.__D[i][j] = self.G.getVertexByID(i).getExeTimeOnMappedProcessor()
                # self.__W[i].append(nx.dijkstra_path_length(self.G.getsdfG(), self.G.getVertexByID(i).getName(), self.G.getVertexByID(j).getName(), 'delay'))
                # path = nx.dijkstra_path(self.G.getsdfG(), self.G.getVertexByID(i).getName(), self.G.getVertexByID(j).getName(), 'delay')
                # d = 0
                # for v in path:
                #     d = d + self.G.getVertexByname(v).getExeTimeOnMappedProcessor()
                # self.__D[i].append(d)

    def Time(self,g: SDFG.SDFgraph, v: DV.Vertex) -> int:
        tg = g
        tgtop = Top.SDFTop(tg)

        time = -1
        if len(tg.getIncomingEdges(v)) == 0:
            time=v.getExeTimeOnMappedProcessor()
        else:
            preTime = -1
            for e in tg.getIncomingEdges(v):
                tt = self.Time(tg,tgtop.getVAL()[tg.getSourceIDofEdge(e)])
                if preTime < tt:
                    preTime = tt
            time = preTime + v.getExeTimeOnMappedProcessor()
        return time

    def clockPeriod(self):
        SubG = self.G.DirectedSubgraph()
        # nx.draw_networkx(SubG.getsdfG())
        # plt.show()
        # Sub_HSDF_CP = HSDF_CP(SubG)
        # Sub_HSDF_CP.HSDF_WD()
        # D = Sub_HSDF_CP.getD()
        # print(Sub_HSDF_CP.dijkstra)
        # print(D)
        CP = -1
        for v in SubG.getVerticesList():
            self.pathTime.append(self.Time(SubG,v))

        for i in range(len(self.pathTime)):
            if CP < self.pathTime[i]:
                CP = self.pathTime[i]
        return CP
