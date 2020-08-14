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
        self.__Vset = []
        self.__Elist = []
        self.__EH = []
        self.__VH = []
        self.__vve = {}

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

        if len(self.__Vset) == 0:
            for v in self.__sdfG.nodes():
                self.__Vset.append(v.getName())
        return self.__Vset

    def getVerticesList(self) -> [DV.Vertex]:
        """

        :return: 返回值是Vertex类型的数组，Vertex有两个属性v.name和v.exeTimeOnMappedProcessor
        """
        if len(self.__Vlist) == 0:
            for v in self.__sdfG.nodes():
                self.__Vlist.append(v)
            return self.__Vlist
        else:
            return self.__Vlist


    def getIDofVertex(self, v: DV.Vertex) -> int:
        """
        :param v: 输入的节点
        :return: 根据节点求他的ID并返回
        """
        if len(self.__Vlist) == 0:
            for vv in self.__sdfG.nodes():
                self.__Vlist.append(vv)
        # for i in range(self.__sdfG.number_of_nodes()):
        #     if self.__Vlist[i].getName() == vw.getName():
        #         return i
        #     if i == int(self.getVertexSize() - 1):
        #         print('没有要找的顶点！')
        return self.__Vlist.index(v)

    def getVertexByname(self, name: str) -> DV.Vertex:
        """
        :param name:输入要查询的节点的name,string类型
        :return:返回name对应的Vertex对象
        """
        if len(self.__Vset) == 0:
            for vv in self.__sdfG.nodes():
                self.__Vset.append(vv.getName())
        if len(self.__Vlist) == 0:
            for vv in self.__sdfG.nodes():
                self.__Vlist.append(vv)

        return self.__Vlist[self.__Vset.index(name)]


    def getVertexByID(self, ID: int) -> DV.Vertex:
        """

        :param ID:输入要查询的ID,从0开始
        :return:返回ID对应的Vertex对象
        """
        if len(self.__Vlist) == 0:
            for vv in self.__sdfG.nodes():
                self.__Vlist.append(vv)

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
        Ev = []
        # for v1, v2, ee in self.__sdfG.edges(data=True):
        #     # print(info['name'])
        #     if v1 == v:
        #         Ev.append(ee['edge'])
        #     if v2 == v:
        #         Ev.append(ee['edge'])
        for em in self.__sdfG.out_edges(v, data=True):
            Ev.append(em[2]['edge'])
        for em in self.__sdfG.in_edges(v, data=True):
            Ev.append(em[2]['edge'])
        return Ev

    def getOutgoingEdges(self, v: DV.Vertex) -> List[DE.SDFedge]:
        """

        :param v: 输入的节点v（Vertex类型）
        :return: 输出从节点v出发的所有边（Edge类型数组）
        """
        outE = []
        # for v1, v2, ee in self.__sdfG.edges(data=True):
        #     if v1 == v:
        #         outE.append(ee['edge'])
        for em in self.__sdfG.out_edges(v, data=True):
            outE.append(em[2]['edge'])
        return outE

    def getIncomingEdges(self, v: DV.Vertex) -> List[DE.SDFedge]:
        """

        :param v: 输入的节点v（Vertex类型）
        :return: 输出以节点v为终点的所有边（Edge类型数组）
        """
        Ev = []
        # for v1, v2, ee in self.__sdfG.edges(data=True):
        #     if v2 == v:
        #         Ev.append(ee['edge'])
        for em in self.__sdfG.in_edges(v, data=True):
            Ev.append(em[2]['edge'])
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
        for v1, v2, ee in self.__sdfG.edges(data=True):
            Eset.append(ee['edge'].getName())
        return Eset

    def getEdgeList(self) -> List[DE.SDFedge]:
        """

        :return: 返回值是Edge类型的数组，Edge有四个属性e.name、e.delay、e.consumeRate、e.produceRate
        """
        if len(self.__Elist) == 0:
            # print('新的')
            for v1, v2, ee in self.__sdfG.edges(data=True):
                self.__Elist.append(ee['edge'])
            return self.__Elist
        else:
            return self.__Elist

    def getIDofEdge(self, e: DE.SDFedge) -> int:
        """

        :param e: 输入的边e(Edge类型)
        :return: 输出边e对应的编号，（从0开始）
        """
        if len(self.__Elist) == 0:
            for v1, v2, ee in self.__sdfG.edges(data=True):
                self.__Elist.append(ee['edge'])

        return self.__Elist.index(e)


    def getEdgeofID(self, eID: int) -> DE.SDFedge:
        """
        :param eID: 传入要找的边的ID
        :return: 输出ID对应的边(Edge类型)
        """
        if len(self.__Elist) == 0:
            for v1, v2, ee in self.__sdfG.edges(data=True):
                self.__Elist.append(ee['edge'])

        if eID < self.__sdfG.number_of_edges():
            return self.__Elist[eID]
        else:
            print('没有要找的边！')

    def getEdgebyVertex(self, v1: DV.Vertex, v2: DV.Vertex) -> [DE.SDFedge]:

        ee = []
        for i in self.__sdfG.get_edge_data(v1, v2):
            ee.append(self.__sdfG.get_edge_data(v1, v2)[i]['edge'])
        return ee



    def getEdgeSource(self, e: DE.SDFedge) -> DV.Vertex:
        """
        :param e: 输入边e（Edge类型）
        :return: 输出边e的出发点
        """
        try:
            return self.__vve[e]['source']
        except Exception:
            print('没有这个节点或找不到这样的边')

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
        try:
            return self.__vve[e]['target']
        except Exception:
            print('没有这个节点或找不到这样的边')

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
        Subgraph = self.getsdfG()
        remove = []
        num = 0
        vv1 = -1
        vv2 = -1
        for v1, v2, ee in self.getsdfG().edges(data=True):
            if v1 == vv1:
                if v2 == vv2:
                    num = num + 1
            if ee['edge'].getDelay() != 0:
                remove.append([v1, v2, num])

            vv1 = v1
            vv2 = v2
        # print('yuan节点信息', Subgraph.nodes(data=True))
        # print('yuan边信息', Subgraph.edges(data=True))
        Subgraph.remove_edges_from(remove)
        # print('zi节点信息', Subgraph.nodes(data=True))
        # print('zi边信息', Subgraph.edges(data=True))

        SubSDFgraph = SDFgraph(Subgraph.name+'_SubSDFgraph')

        for vv in Subgraph.nodes():
            # v = DV.Vertex(name, weight['exeTimeOnMappedProcessor'])
            SubSDFgraph.addVertex(vv)
        for v1, v2, ee in Subgraph.edges(data=True):
            # print(v1+v2+str(info))
            # e = DE.SDFedge(info['name'], info['delay'], info['produceRate'], info['consumeRate'])
            # print('v1:'+v1)
            # print('v2:'+v2)
            # print(self.getVertexByname(v1).getName())
            # print(self.getVertexByname(v2).getName())
            # print('v1:::'+v1)
            # print('v2:::'+v2)
            SubSDFgraph.addEdge(v1, v2, ee['edge'])
        return SubSDFgraph

    # def setEdgeDelay(self, e: DE.SDFedge, d: int):
    #     ee = e
    #     ee.setDelay(d)
    #
    #     num = 0
    #     vv1 = -1
    #     vv2 = -1
    #     for v1, v2, info in self.getsdfG().edges(data=True):
    #         # print(self.getsdfG().edges(data=True))
    #         if v1 == vv1:
    #             if v2 == vv2:
    #                 num = num + 1
    #         if info['name'] == e.getName():
    #             remove = [v1, v1, num]
    #             break
    #     # print('yici------------------------------------------------')
    #
    #     v1 = self.getEdgeSource(e)
    #     v2 = self.getEdgeTarget(e)
    #     self.getsdfG().remove_edge(self.getEdgeSource(e).getName(), self.getEdgeTarget(e).getName(), num)
    #     # print(ee.getDelay())
    #     self.addEdge(v1, v2, ee)
    #     # print('加边之后')
    #     # print(self.getsdfG().edges(data=True))
    #
    # def setEdgeproduceRate(self, e: DE.SDFedge, produceRate: int):
    #     ee = e
    #     ee.setProduceRate(produceRate)
    #
    #     num = 0
    #     vv1 = -1
    #     vv2 = -1
    #     for v1, v2, info in self.getsdfG().edges(data=True):
    #         if v1 == vv1:
    #             if v2 == vv2:
    #                 num = num + 1
    #         if info['name'] == e.getName():
    #             remove = [v1, v1, num]
    #             break
    #
    #     v1 = self.getEdgeSource(e)
    #     v2 = self.getEdgeTarget(e)
    #     self.getsdfG().remove_edge(self.getEdgeSource(e).getName(), self.getEdgeTarget(e).getName(), num)
    #     self.addEdge(v1, v2, ee)
    #
    # def setEdgeconsumeRate(self, e: DE.SDFedge, consumeRate: int):
    #     ee = e
    #     ee.setConsumeRate(consumeRate)
    #
    #     num = 0
    #     vv1 = -1
    #     vv2 = -1
    #     for v1, v2, info in self.getsdfG().edges(data=True):
    #         if v1 == vv1:
    #             if v2 == vv2:
    #                 num = num + 1
    #         if info['name'] == e.getName():
    #             remove = [v1, v1, num]
    #             break
    #
    #     v1 = self.getEdgeSource(e)
    #     v2 = self.getEdgeTarget(e)
    #     self.getsdfG().remove_edge(self.getEdgeSource(e).getName(), self.getEdgeTarget(e).getName(), num)
    #     self.addEdge(v1, v2, ee)
    #
    # def setVertexexeTime(self, v: DV.Vertex, exeTime: int):
    #     vv = v
    #     vv.setExeTimeOnMappedProcessor(exeTime)
    #     self.addVertex(vv)


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
        self.__VH.append(v)
        self.__sdfG.add_node(v)

    def addEdge(self, v1: DV.Vertex, v2: DV.Vertex, e: DE.SDFedge):
        """

        :param v1: 边的源点
        :param v2: 边的汇点
        :param e: Edge类型数据
        :return: 将边添加到图中
        """
        self.__EH.append(e)
        self.__vve[e] = {'source': v1, 'target': v2}
        self.__sdfG.add_edge(v1, v2, edge=e)

    def nodes(self):
        vset = []
        for v in self.getVerticesList():
            vset.append((v.getName(), v.getExeTimeOnMappedProcessor()))
        return vset

    def edges(self):
        eset = []
        for v1, v2, ee in self.__sdfG.edges(data=True):
            eset.append((v1.getName(), v2.getName(), ee['edge'].getName(),
                         {'delay', ee['edge'].getDelay()},
                         {'produceRate', ee['edge'].getProduceRate()},
                         {'consumeRate', ee['edge'].getConsumeRate()}))
        return eset

    def copySDFG(self, mess=''):
        gg = SDFgraph(self.getName()+'_copy'+mess)
        for v in self.getVerticesList():
            vv = DV.Vertex(v.getName(), v.getExeTimeOnMappedProcessor())
            gg.addVertex(vv)

        for e in self.getEdgeList():
            ee = DE.SDFedge(e.getName(), e.getDelay(), e.getProduceRate(), e.getConsumeRate())
            v1 = gg.getVertexByname(self.getEdgeSource(e).getName())
            v2 = gg.getVertexByname(self.getEdgeTarget(e).getName())
            gg.addEdge(v1, v2, ee)
        return gg

    # def Refresh(self):
    #     # refreshg = SDFgraph(self.__name)
    #     # self.__VH.sort(key=self.sortkey())
    #     # self.__EH.sort(key=self.sortkey())
    #     # for v in self.__VH:
    #     #     refreshg.addVertex(v)
    #     # for e in self.__EH:
    #     #     refreshg.addEdge(self.getEdgeSource(e))
    #     for v in self.getVerticesSet():
    #         self.__sdfG.nodes[v]['exeTimeOnMappedProcessor'] = \
    #             self.__sdfG.nodes[v]['vmess'].getExeTimeOnMappedProcessor()
    #
    #     for v1, v2, info in self.__sdfG.edges(data=True):
    #         # print(v1)
    #         # print(v2)
    #         self.__sdfG[v1][v2][0]['name'] = self.__sdfG[v1][v2][0]['emess'].getName()
    #         self.__sdfG[v1][v2][0]['delay'] = self.__sdfG[v1][v2][0]['emess'].getDelay()
    #         self.__sdfG[v1][v2][0]['consumeRate'] = self.__sdfG[v1][v2][0]['emess'].getConsumeRate()
    #         self.__sdfG[v1][v2][0]['produceRate'] = self.__sdfG[v1][v2][0]['emess'].getProduceRate()
