import networkx as nx
from sympy import lcm

from sdfGraph import DefVertex as DV
from sdfGraph import DefEdge as DE
from sdfGraph import SDFgraph
from typing import List
from fractions import Fraction


class SDFTop:
    __RepVector: List[Fraction]

    def __init__(self, g: SDFgraph.SDFgraph):
        self.__sdfG = g
        self.__verticeAL = g.getVerticesList()
        self.__edgesAL = g.getEdgeList()
        self.__numEdges = g.getEdgeSize()
        self.__numVertices = g.getVertexSize()
        self.__RepVector = []

    def getsdfG(self):
        return self.__sdfG

    def getVAL(self):
        return self.__verticeAL

    def getEAL(self):
        return self.__edgesAL

    # compute the production rate vector (index by edge)
    def getProdVector(self) -> List[int]:
        intProdVector = []
        for i in range(self.__numEdges):
            intProdVector.append(self.__edgesAL[i].getProduceRate())
        return intProdVector

    # compute the consumption rate vector (index by edge)
    def getConsVector(self) -> List[int]:
        intConsVector = []
        for i in range(self.__numEdges):
            intConsVector.append(self.__edgesAL[i].getConsumeRate())
        return intConsVector

    # get delay on each edges
    def getDelayVector(self) -> List[int]:
        intDelayVector = []
        for i in range(self.__numEdges):
            intDelayVector.append(self.__edgesAL[i].getDelay())
        return intDelayVector

    # get the topologic matrix of the SDF
    def getTMatrix(self) -> List[list]:
        TMatrix = []
        for i in range(self.__numEdges):
            TMatrix.append([])
            for j in range(self.__numVertices):
                TMatrix[i].append(0)

        for i in range(self.__numEdges):
            TMatrix[i][self.__sdfG.getSourceIDofEdge(self.__edgesAL[i])] = self.getProdVector()[i]
            TMatrix[i][self.__sdfG.getTargetIDofEdge(self.__edgesAL[i])] = -1*self.getConsVector()[i]

        return TMatrix

    def getRepVector(self):
        intRepVector = []
        for i in range(self.__numVertices):
            self.__RepVector.append(Fraction(0))
            # print(self.__RepVector)

        self.setReps(0, Fraction(1))

        # compute all actors' denominator's least common multiply
        x = 1
        for i in range(self.__numVertices):
            x = lcm(x, self.__RepVector[i].denominator)

        # set each actors' value equals x*reps(A)
        y = Fraction(int(x))
        for i in range(self.__numVertices):
            # self.__RepVector[i] = y.__mul__(self.__RepVector[i])
            self.__RepVector[i] = Fraction.__mul__(y, self.__RepVector[i])
            intRepVector.append(self.__RepVector[i].numerator)

        # check if it exists error
        for e in self.__edgesAL:
            if intRepVector[self.__sdfG.getSourceIDofEdge(e)]*e.getProduceRate() != \
                    intRepVector[self.__sdfG.getTargetIDofEdge(e)]*e.getConsumeRate():
                return None

        return intRepVector

    def setReps(self, k: int, n: Fraction):
        self.__RepVector[k] = n

        # each output edge of actor whose index is k
        for e in self.__sdfG.getOutgoingEdges(self.__verticeAL[k]):
            i = self.__sdfG.getTargetIDofEdge(e)
            if self.__RepVector[i].numerator == 0:
                # print(e.getConsumeRate())
                # print(e.getProduceRate())
                # print(Fraction(e.getProduceRate(), e.getConsumeRate()))
                # print(' ')
                r = n.__mul__(Fraction(e.getProduceRate(), e.getConsumeRate()))
                self.setReps(i, r)

        # each input edge of actor whose index is k
        for e in self.__sdfG.getIncomingEdges(self.__verticeAL[k]):
            i = self.__sdfG.getSourceIDofEdge(e)
            if self.__RepVector[i].numerator == 0:
                r = n.__mul__(Fraction(e.getConsumeRate(), e.getProduceRate()))
                self.setReps(i, r)
