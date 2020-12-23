class SDFedge:
    def __init__(self, name, delay=0, produceRate=1, consumeRate=1, tranTime=1):
        self.__name = name  # instance variable unique to each instance
        self.__produceRate = produceRate
        self.__consumeRate = consumeRate
        self.__tranTime = tranTime

        self.__delay = delay

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setDelay(self, delay):
        self.__delay = delay

    def getDelay(self):
        return self.__delay

    def setConsumeRate(self, consumeRate):
        self.__consumeRate = consumeRate

    def getConsumeRate(self):
        return self.__consumeRate

    def setProduceRate(self, produceRate):
        self.__produceRate = produceRate

    def getProduceRate(self):
        return self.__produceRate

    def gettranTime(self):
        return self.__tranTime

    def settranTime(self, tranTime):
        self.__tranTime = tranTime
