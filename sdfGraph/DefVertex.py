class Vertex:
    def __init__(self, name, exeTimeOnMappedProcessor=1):
        self.__name = name  # instance variable unique to each instance
        # self.consumeRate = consumeRate
        # self.produceRate = produceRate
        self.__exeTimeOnMappedProcessor = exeTimeOnMappedProcessor



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

    # def setconsumeRate(self,consumeRate):
    #     self.consumeRate = consumeRate
    #
    # def setproduceRate(self,produceRate):
    #     self.produceRate = produceRate
