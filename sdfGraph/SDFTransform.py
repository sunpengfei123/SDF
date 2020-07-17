from sdfGraph import SDFgraph
from sdfGraph import SDFTop


class SDFTransform:
    def __init__(self, g: SDFgraph.SDFgraph):
        self.ginitial = g
        gg = g.copySDFG()
        self.sdfG = gg

    def retimeSDF(self, r: list):
        rG = SDFgraph.SDFgraph('Retimed_'+str(self.sdfG.getName()))
        self.sdfG = self.ginitial.copySDFG()
        aTop = SDFTop.SDFTop(self.sdfG)

        # create vertices
        for v in aTop.getVAL():
            newV = v
            # newV = DefVertex.Vertex(v.getName(), v.getExeTimeOnMappedProcessor())
            rG.addVertex(newV)

        # create edges
        for e in aTop.getEAL():
            newE = e
            rG.addEdge(aTop.getVAL()[self.sdfG.getSourceIDofEdge(e)], aTop.getVAL()[self.sdfG.getTargetIDofEdge(e)], newE)

        VL = aTop.getVAL()
        EL = aTop.getEAL()

        # reset delay value
        rGTop = SDFTop.SDFTop(rG)
        ee = rGTop.getEAL()
        for i in range(len(rGTop.getEAL())):
            e = rGTop.getEAL()[i]
            delayofE = e.getDelay()

            indexS = rG.getSourceIDofEdge(e)
            indexT = rG.getTargetIDofEdge(e)
            # print('delayofE:' + str(delayofE))
            # print(rGTop.getVAL()[indexS].getName()+str(indexS)+'   '+str(r[indexS]))
            # print(rGTop.getVAL()[indexT].getName()+str(indexT)+'   '+str(r[indexT]))
            newDelayofE = delayofE +r[indexT]*e.getConsumeRate() - r[indexS]*e.getProduceRate()
            # print('newDelayofE:' + str(newDelayofE))
            e.setDelay(newDelayofE)
            rG.Refresh()
            # print('new图：')
            # print(rG.getsdfG().edges(data=True))
            # ee[i].setDelay(newDelayofE)
        # print('之前')
        # print(rG.getsdfG().edges(data=True))
        # for e in ee:
        #     # print(e.getName())
        #     # print(e.getDelay())
        #     rG.setEdgeDelay(e, e.getDelay())
        # print('之后')
        # print(rG.getsdfG().edges(data=True))

        return rG