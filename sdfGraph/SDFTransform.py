from sdfGraph import SDFgraph
from sdfGraph import SDFTop


class SDFTransform:
    def __init__(self, g: SDFgraph.SDFgraph):
        self.sdfG = g

    def retimeSDF(self, r: list):
        rG = SDFgraph.SDFgraph('Retimed_'+str(self.sdfG.getName()))
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

        # reset delay value
        rGTop = SDFTop.SDFTop(rG)
        for e in rGTop.getEAL():
            delayofE = e.getDelay()

            indexS = rG.getSourceIDofEdge(e)
            indexT = rG.getTargetIDofEdge(e)

            newDelayofE = delayofE + r[indexT]*e.getConsumeRate() - r[indexS]*e.getProduceRate()

            e.setDelay(newDelayofE)

        return rG