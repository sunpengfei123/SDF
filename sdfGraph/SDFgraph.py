import networkx as nx
from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE
from typing import List

# from sdfGraph.DefVertex import Vertex


class SDFgraph:
    __Vlist: List[DV.Vertex]
    __Elist: List[DE.SDFedge]

    def __init__(self, name):
        self.__name = name  # instance variable unique to each instance
        self.__sdfG = nx.MultiDiGraph()
        self.__Vlist = []
        self.__Elist = []

    def setName(self, name):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def getsdfG(self):
        return self.__sdfG

    def getVertexSize(self) -> int:
        """

        :return: 返回图中节点个数
        """
        return self.__sdfG.number_of_nodes()

    # get the vertex set
    def getVerticesSet(self) -> List[str]:
        """

        :return: 返回值是String类型的数组，是所有顶点名字的序列
        """
        Vset = []
        for name, weight in self.__sdfG.nodes(data=True):
            Vset.append(name)
        return Vset

    def getVerticesList(self) -> [DV.Vertex]:
        """

        :return: 返回值是Vertex类型的数组，Vertex有两个属性v.name和v.exeTimeOnMappedProcessor
        """
        if len(self.__Vlist) == 0:
            for name, weight in self.__sdfG.nodes(data=True):
                v = DV.Vertex(name, weight['exeTimeOnMappedProcessor'])
                self.__Vlist.append(v)
            return self.__Vlist
        else:
            return self.__Vlist


    def getIDofVertex(self, v: DV.Vertex) -> int:
        """
        :param v: 输入的节点
        :return: 根据节点求他的ID并返回
        """
        v = v
        if len(self.__Vlist) == 0:
            for name, weight in self.__sdfG.nodes(data=True):
                v = DV.Vertex(name, weight['exeTimeOnMappedProcessor'])
                self.__Vlist.append(v)
        for i in range(self.__sdfG.number_of_nodes()):
            if self.__Vlist[i].getName() == v.getName():
                return i
            if i == int(self.getVertexSize() - 1):
                print('没有要找的顶点！')

    def getVertexByname(self, name: str) -> DV.Vertex:
        """
        :param name:输入要查询的节点的name,string类型
        :return:返回name对应的Vertex对象
        """
        if len(self.__Vlist) == 0:
            for name, weight in self.__sdfG.nodes(data=True):
                v = DV.Vertex(name, weight['exeTimeOnMappedProcessor'])
                self.__Vlist.append(v)

        for i in self.__Vlist:
            if i.getName() == name:
                return i


    def getVertexByID(self, ID: int) -> DV.Vertex:
        """

        :param ID:输入要查询的ID,从0开始
        :return:返回ID对应的Vertex对象
        """
        if len(self.__Vlist) == 0:
            for name, weight in self.__sdfG.nodes(data=True):
                v = DV.Vertex(name, weight['exeTimeOnMappedProcessor'])
                self.__Vlist.append(v)

        if ID < self.__sdfG.number_of_nodes():
            return self.__Vlist[ID]
        else:
            print('没有要找的顶点！')


    def getDegreeofVertex(self, v: DV.Vertex) -> int:
        """

        :param v: 输入节点（Vertex类型）
        :return: 输出v的度数（出度入度之和）
        """
        return len(self.getEdgesofVertex(v))

    def getEdgesofVertex(self, v: DV.Vertex) -> List[DE.SDFedge]:
        """

        :param v: 输入的节点v（Vertex类型）
        :return: 输出和节点v相连的所有边（Edge类型数组）
        """
        E = self.getEdgeList()
        Ev = []
        for v1, v2, info in self.__sdfG.edges(data=True):
            print(info['name'])
            if v1 == v.getName():
                for e in E:
                    if e.getName() == info['name']:
                        print('you')
                        Ev.append(e)
            if v2 == v.getName():
                for e in E:
                    if e.getName() == info['name']:
                        print('you')
                        Ev.append(e)
        return Ev

    def getOutgoingEdges(self, v: DV.Vertex) -> List[DE.SDFedge]:
        """

        :param v: 输入的节点v（Vertex类型）
        :return: 输出从节点v出发的所有边（Edge类型数组）
        """
        E = self.getEdgeList()
        outE = []
        for v1, v2, info in self.__sdfG.edges(data=True):
            if v1 == v.getName():
                for e in E:
                    if e.getName() == info['name']:

                        outE.append(e)
        return outE

    def getIncomingEdges(self, v: DV.Vertex) -> List[DE.SDFedge]:
        """

        :param v: 输入的节点v（Vertex类型）
        :return: 输出以节点v为终点的所有边（Edge类型数组）
        """
        E = self.getEdgeList()
        Ev = []
        for v1, v2, info in self.__sdfG.edges(data=True):
            if v2 == v.getName():
                for e in E:
                    if e.getName() == info['name']:
                        Ev.append(e)
        return Ev

    def getOutDegree(self, v: DV.Vertex):
        """

        :param v: 输入节点v（Vertex类型）
        :return:输出节点的出度
        """
        Ev = self.getOutgoingEdges(v)
        return len(Ev)

    def getInDegree(self, v: DV.Vertex):
        """

        :param v: 输入节点v（Vertex类型）
        :return:输出节点的入度
        """
        Ev = self.getIncomingEdges(v)
        return len(Ev)

    def getEdgeSize(self):
        """

        :return: 图中边的个数
        """
        return self.__sdfG.number_of_edges()

    def getAllOutgoingEdgeID(self, vID: int):
        """

        :param vID: 传入节点的ID
        :return: 返回节点所有出边的ID数组
        """
        v = self.getVertexByID(vID)
        E = self.getOutgoingEdges(v)
        eID = []
        for e in E:
            eID.append(self.getIDofEdge(e))

        return eID

    def getAllIncomingEdgeID(self, vID: int):
        """

        :param vID: 传入节点的ID
        :return: 返回节点所有入边的ID数组
        """
        v = self.getVertexByID(vID)
        E = self.getIncomingEdges(v)
        eID = []
        for e in E:
            eID.append(self.getIDofEdge(e))

        return eID

    # get the vertex set
    def getEdgeSet(self):
        """

        :return: 返回所有边名字组成的序列
        """
        Eset = []
        for v1, v2, info in self.__sdfG.edges(data=True):
            Eset.append(info['name'])
        return Eset

    def getEdgeList(self) -> List[DE.SDFedge]:
        """

        :return: 返回值是Edge类型的数组，Edge有四个属性e.name、e.delay、e.consumeRate、e.produceRate
        """
        if len(self.__Elist) == 0:
            # print('新的')
            for v1, v2, info in self.__sdfG.edges(data=True):
                e = DE.SDFedge(info['name'], info['delay'], info['produceRate'], info['consumeRate'])
                self.__Elist.append(e)
            return self.__Elist
        else:
            return self.__Elist

    def getIDofEdge(self, e: DE.SDFedge) -> int:
        """

        :param e: 输入的边e(Edge类型)
        :return: 输出边e对应的编号，（从0开始）
        """
        if len(self.__Elist) == 0:
            for v1, v2, info in self.__sdfG.edges(data=True):
                e = DE.SDFedge(info['name'], info['delay'], info['consumeRate'], info['produceRate'])
                self.__Elist.append(e)

        for i in range(self.__sdfG.number_of_edges()):
            if e.getName() == self.__Elist[i].getName():
                return i
            if i == int(self.getEdgeSize() - 1):
                print('没有要找的边！')


    def getEdgeofID(self, eID: int) -> DE.SDFedge:
        """
        :param eID: 传入要找的边的ID
        :return: 输出ID对应的边(Edge类型)
        """
        if len(self.__Elist) == 0:
            for v1, v2, info in self.__sdfG.edges(data=True):
                e = DE.SDFedge(info['name'], info['delay'], info['consumeRate'], info['produceRate'])
                self.__Elist.append(e)
        if eID < self.__sdfG.number_of_edges():
            return self.__Elist[eID]
        else:
            print('没有要找的边！')

    def getEdgebyVertex(self, v1: DV.Vertex, v2: DV.Vertex) -> DE.SDFedge:
        for vv1, vv2, info in self.__sdfG.edges(data=True):
            if vv1 == v1.getName():
                if vv2 == v2.getName():
                    return DE.SDFedge(info['name'], info['delay'], info['consumeRate'], info['produceRate'])
        print('么有从'+str(v1.getName())+'到'+str(v2.getName())+'的边')
        return -1

    def getEdgeSource(self, e: DE.SDFedge) -> DV.Vertex:
        """
        :param e: 输入边e（Edge类型）
        :return: 输出边e的出发点
        """
        for v1, v2, info in self.__sdfG.edges(data=True):
            if e.getName() == info['name']:
                v = self.getVertexByname(v1)
                return v

    def getSourceIDofEdge(self, e: DE.SDFedge) -> int:
        """

        :param e: 输入边e（Edge类型）
        :return: 返回边e出发节点的ID
        """
        return self.getIDofVertex(self.getEdgeSource(e))

    def getTargetIDofEdge(self, e: DE.SDFedge) -> int:
        """
        :param e: 输入边e（Edge类型）
        :return: 返回边e目标节点的ID
        """
        return self.getIDofVertex(self.getEdgeTarget(e))


    def getEdgeTarget(self, e: DE.SDFedge) -> DV.Vertex:
        """
        :param e: 输入边e(Edge类型)
        :return: 返回e的目标节点
        """
        for v1, v2, info in self.__sdfG.edges(data=True):
            if e.getName() == info['name']:
                v = self.getVertexByname(v2)
                return v

    def getAllOutgoingVertexIDs(self, v: DV.Vertex) -> List[int]:
        """

        :param v: 输入节点v（Vertex类型 ）
        :return: 返回从v出发，能到达的所有节点的ID
        """
        vID = []
        eList = self.getOutgoingEdges(v)
        for e in eList:
            vv = self.getTargetIDofEdge(e)
            vID.append(vv)
        return vID

    def getAllOutgoingVertexs(self, v: DV.Vertex) -> List[DV.Vertex]:
        """

        :param v: 输入节点v（Vertex类型 ）
        :return: 返回从v出发，能到达的所有节点列表
        """
        vList = []
        eList = self.getOutgoingEdges(v)
        for e in eList:
            vv = self.getEdgeTarget(e)
            vList.append(vv)
        return vList

    def DirectedSubgraph(self):
        Subgraph =self.getsdfG()
        remove = []
        num = 0
        vv1 = -1
        vv2 = -1
        for v1, v2, info in self.getsdfG().edges(data=True):
            if v1 == vv1:
                if v2 == vv2:
                    num = num + 1
            if info['delay'] != 0:
                remove.append([v1, v2, num])

            vv1 = v1
            vv2 = v2
        Subgraph.remove_edges_from(remove)
        SubSDFgraph = SDFgraph(Subgraph.name+'_SubSDFgraph')
        for name, weight in Subgraph.nodes(data=True):
            v = DV.Vertex(name, weight['exeTimeOnMappedProcessor'])
            SubSDFgraph.addVertex(v)
        for v1, v2, info in Subgraph.edges(data=True):
            e = DE.SDFedge(info['name'], info['delay'], info['produceRate'], info['consumeRate'])
            SubSDFgraph.addEdge(self.getVertexByname(v1), self.getVertexByname(v2), e)
        return SubSDFgraph


    def getAllIncomingVertexIDs(self, v: DV.Vertex) -> List[int]:
        """

        :param v: 输入节点v（Vertex类型 ）
        :return: 返回能到达v的所有节点ID
        """
        vID = []
        eList = self.getIncomingEdges(v)
        for e in eList:
            vv = self.getSourceIDofEdge(e)
            vID.append(vv)
        return vID

    def getAllIncomingVertexs(self, v: DV.Vertex) -> List[DV.Vertex]:
        """

        :param v: 输入节点v（Vertex类型 ）
        :return: 返回能到达v的所有节点列表
        """
        vList = []
        eList = self.getIncomingEdges(v)
        for e in eList:
            vv = self.getEdgeSource(e)
            vList.append(vv)
        return vList

    def addVertex(self, v: DV.Vertex):
        """

        :param v: 传入一个Vertex类型数据
        :return: 将该节点添加到图中
        """
        self.__sdfG.add_node(v.getName(), exeTimeOnMappedProcessor=v.getExeTimeOnMappedProcessor())

    def addEdge(self, v1: DV.Vertex, v2: DV.Vertex, e: DE.SDFedge):
        """

        :param v1: 边的源点
        :param v2: 边的汇点
        :param e: Edge类型数据
        :return: 将边添加到图中
        """

        self.__sdfG.add_edge(v1.getName(), v2.getName(), name=e.getName(), delay=e.getDelay(),
                             consumeRate=e.getConsumeRate(), produceRate=e.getProduceRate())
