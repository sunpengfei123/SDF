class Vertex:

    def __init__(self, name, exeTimeOnMappedProcessor=1, mappedProcessorType = "p0"):
        self.__name = name  # instance variable unique to each instance
        # self.consumeRate = consumeRate
        # self.produceRate = produceRate
        self.__exeTimeOnMappedProcessor = exeTimeOnMappedProcessor
        self.__mappedProcessorType = mappedProcessorType
        self.__processorTypeNameArray = [mappedProcessorType]
        self.__processorAndexetimeDict = {mappedProcessorType: exeTimeOnMappedProcessor}


    def setName(self, name):
        self.__name = name

    def getName(self) -> str:
        """

        :rtype: str
        """
        return self.__name

    def setExeTimeOnMappedProcessor(self, exeTimeOnMappedProcessor):
        self.__exeTimeOnMappedProcessor = exeTimeOnMappedProcessor

    def getExeTimeOnMappedProcessor(self):
        return self.__exeTimeOnMappedProcessor

    def setProcessorTypeNameArray(self, processorTypeNameArray):
        self.__processorTypeNameArray = processorTypeNameArray

    def getProcessorTypeNameArray(self):
        return self.__processorTypeNameArray

    # def setExecutionTimeArray(self, ExecutionTimeArray):
    #     self.__ExecutionTimeArray = ExecutionTimeArray
    #
    # def getExecutionTimeArray(self):
    #     return self.__ExecutionTimeArray

    def setmappedProcessorType(self, mappedProcessorType):
        self.__mappedProcessorType = mappedProcessorType

    def getMappedProcessorType(self):
        return self.__mappedProcessorType

    def getprocessorAndexetimeDict(self):
        return self.__processorAndexetimeDict

    def setprocessorAndexetimeDict(self, processorAndexetimeDict):
        self.__processorAndexetimeDict = processorAndexetimeDict

    def addNewProcessorType(self, processorTypeName, executionTime):
        if not self.__processorAndexetimeDict.__contains__(processorTypeName):
            self.__processorAndexetimeDict[processorTypeName] = executionTime
        if not self.__processorTypeNameArray.__contains__(processorTypeName):
            self.__processorTypeNameArray.append(processorTypeName)


    # def setconsumeRate(self,consumeRate):
    #     self.consumeRate = consumeRate
    #
    # def setproduceRate(self,produceRate):
    #     self.produceRate = produceRate
