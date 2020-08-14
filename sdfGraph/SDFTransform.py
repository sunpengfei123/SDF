from sdfGraph import SDFgraph
from sdfGraph import SDFTop
from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE

class SDFTransform:
    def __init__(self, g: SDFgraph.SDFgraph):
        self.ginitial = g
        gg = g.copySDFG()
        self.sdfG = gg
        self.rG = g.copySDFG('retime')

    def retimeSDF(self, r: list):
        # rG = SDFgraph.SDFgraph('Retimed_'+str(self.sdfG.getName()))
        # aTop = SDFTop.SDFTop(self.sdfG)
        #
        # # create vertices
        # for v in aTop.getVAL():
        #     newV = DV.Vertex(v.getName(), v.getExeTimeOnMappedProcessor())
        #     rG.addVertex(newV)
        #
        # # create edges
        # for e in aTop.getEAL():
        #     newE = DE.SDFedge(e.getName(), e.getDelay(), e.getProduceRate(), e.getConsumeRate())
        #     for v in rG.getVerticesList():
        #         if v.getName() == self.sdfG.getEdgeSource(e).getName():
        #             v1 = v
        #         if v.getName() == self.sdfG.getEdgeTarget(e).getName():
        #             v2 = v
        #     rG.addEdge(v1, v2, newE)
        #
        # VL = aTop.getVAL()
        # EL = aTop.getEAL()

        for e in self.rG.getEdgeList():
            e.setDelay(self.sdfG.getEdgeList()[self.rG.getEdgeList().index(e)].getDelay())

        # reset delay value
        rGTop = SDFTop.SDFTop(self.rG)
        ee = rGTop.getEAL()
        for i in range(len(rGTop.getEAL())):
            e = rGTop.getEAL()[i]
            delayofE = e.getDelay()

            indexS = self.rG.getSourceIDofEdge(e)
            indexT = self.rG.getTargetIDofEdge(e)
            # print('delayofE:' + str(delayofE))
            # print(rGTop.getVAL()[indexS].getName()+str(indexS)+'   '+str(r[indexS]))
            # print(rGTop.getVAL()[indexT].getName()+str(indexT)+'   '+str(r[indexT]))
            newDelayofE = delayofE +r[indexT]*e.getConsumeRate() - r[indexS]*e.getProduceRate()
            # print('newDelayofE:' + str(newDelayofE))
            e.setDelay(newDelayofE)
            # print('new图：')
            # print(rG.edges())
            # ee[i].setDelay(newDelayofE)
        # print('之前')
        # print(rG.getsdfG().edges(data=True))
        # for e in ee:
        #     # print(e.getName())
        #     # print(e.getDelay())
        #     rG.setEdgeDelay(e, e.getDelay())
        # print('之后')
        # print(rG.getsdfG().edges(data=True))

        return self.rG