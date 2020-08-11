import sys
import threading

import networkx as nx
import matplotlib.pyplot as plt

from sdfGraph import DefVertex as DV
from sdfGraph import SDFgraph as SDFG
from sdfGraph import DefEdge as DE
from sdfGraph import SDFTop as Top

sys.setrecursionlimit(1000000)

class HSDF_CP:
    def __init__(self, g: SDFG.SDFgraph):
        gg = g.copySDFG()
        self.G = gg
        self.__W = []
        self.__D = []
        self.atop = Top.SDFTop(gg)
        self.dijkstra = []
        self.pathTime = []

    def getW(self):
        return self.__W

    def getD(self):
        return self.__D

    def HSDF_WD(self):
        N = self.G.getVertexSize()
        weight = []
        Max = 20

        # 初始化W和D
        for i in range(N):
            self.dijkstra.append([])
            self.__W.append([])
            self.__D.append([])
            weight.append([])
            for j in range(N):
                self.dijkstra[i].append([])
                self.__W[i].append([])
                self.__D[i].append([])
                weight[i].append([])
                for k in range(2):
                    weight[i][j].append(0)

        # for i in range(self.G.getVertexSize()):
        #     for j in range(self.G.getVertexSize()):
        #         if i != j:
        #             try:
        #                 self.dijkstra[i][j] = nx.dijkstra_path(self.G.getsdfG(), self.G.getVertexByID(i), self.G.getVertexByID(j), 'delay')
        #                 self.__W[i][j] = nx.dijkstra_path_length(self.G.getsdfG(), self.G.getVertexByID(i), self.G.getVertexByID(j), 'delay')
        #                 path = nx.dijkstra_path(self.G.getsdfG(), self.G.getVertexByID(i).getName(),
        #                                         self.G.getVertexByID(j).getName(), 'delay')
        #                 d = 0
        #                 for v in path:
        #                     d = d + self.G.getVertexByname(v).getExeTimeOnMappedProcessor()
        #                 self.__D[i][j] = d
        #             except:
        #
        #                 self.dijkstra[i][j] = -1
        #                 self.__W[i][j] = -1
        #                 self.__D[i][j] = -1
        #         else:
        #             self.dijkstra[i][j] = self.G.getVertexByID(i)
        #             self.__W[i][j] = -1
        #             self.__D[i][j] = self.G.getVertexByID(i).getExeTimeOnMappedProcessor()
        #         # self.__W[i].append(nx.dijkstra_path_length(self.G.getsdfG(), self.G.getVertexByID(i).getName(), self.G.getVertexByID(j).getName(), 'delay'))
        #         # path = nx.dijkstra_path(self.G.getsdfG(), self.G.getVertexByID(i).getName(), self.G.getVertexByID(j).getName(), 'delay')
        #         # d = 0
        #         # for v in path:
        #         #     d = d + self.G.getVertexByname(v).getExeTimeOnMappedProcessor()
        #         # self.__D[i].append(d)

        # step 1
        for i in range(N):
            for j in range(N):
                if i != j:
                    weight[i][j][0] = Max

        for v in self.G.getVerticesList():
            i = self.G.getIDofVertex(v)
            # i = self.atop.getVAL().index(v)

            for e in self.G.getOutgoingEdges(v):
                j = self.G.getIDofVertex(self.G.getEdgeTarget(e))

                weight[i][j][0] = e.getDelay()
                weight[i][j][1] = -1*v.getExeTimeOnMappedProcessor()
        # end step 1

        # step 2
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if (weight[i][k][0] + weight[k][j][0]) < weight[i][j][0]:
                        print('asdfasd')
                        print(weight[i][k][0])
                        print(weight[k][j][0])
                        print(weight[i][j][0])
                        weight[i][j][0] = weight[i][k][0] + weight[k][j][0]
                        weight[i][j][1] = weight[i][k][1] + weight[k][j][1]
                    else:
                        if (weight[i][k][0]+weight[k][j][0]) == weight[i][j][0]:
                            if (weight[i][k][1]+weight[k][j][1]) < weight[i][j][1]:
                                weight[i][j][1] = weight[i][k][1] + weight[k][j][1]
        # end step 2

        # step 3
        for i in range(N):
            for j in range(N):
                self.__W[i][j] = weight[i][j][0]
                tempV = self.G.getVertexByID(j)
                self.__D[i][j] = tempV.getExeTimeOnMappedProcessor() - weight[i][j][1]


    def Time(self,g: SDFG.SDFgraph, v: DV.Vertex) -> int:
        tg = g
        tgtop = Top.SDFTop(tg)

        time = -1
        # print(v.getName())
        # print(len(tg.getIncomingEdges(v)))
        if len(tg.getIncomingEdges(v)) == 0:
            time=v.getExeTimeOnMappedProcessor()
        else:
            preTime = -1
            for e in tg.getIncomingEdges(v):
                # print(e.getName())
                # print(tgtop.getVAL()[tg.getSourceIDofEdge(e)].getName()+'Source_name')
                # print(tgtop.getVAL()[tg.getTargetIDofEdge(e)].getName() + 'Target_name')
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
            # print(v.getName())
            self.pathTime.append(self.Time(SubG,v))

        for i in range(len(self.pathTime)):
            if CP < self.pathTime[i]:
                CP = self.pathTime[i]
        return CP

    if __name__ == "__main__":
        threading.stack_size(200000000)
        thread = threading.Thread(target=clockPeriod())
        thread.start()