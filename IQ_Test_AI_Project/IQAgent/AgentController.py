from IQAgent import Number, Direction, OddOneOut, Agent

class AgentController():
    def __init__(self):
        self.myAgent = Agent.Agent()
        self.AgentCollection = [Number.Number(), Direction.Direction(), OddOneOut.OddOneOut()]
        self.answers = []

    def inputText(self, input):
        self.myAgent.setInputText(input)

    def getAgent(self, agentNum):
        if agentNum == 0:
            return self.myAgent
        else:
            return self.AgentCollection[agentNum-1]

    def getAnswer(self, returnType):
        if self.myAgent.getInputText() != "":
            type = self.myAgent.checkType()
            self.AgentCollection[type-1].setInputText(self.myAgent.getInputText())
            self.AgentCollection[type-1].getMultipleChoice()
            self.AgentCollection[type-1].solve()
            self.myAgent.setInputText("")
            if returnType == 1:
                return self.AgentCollection[type-1].getAnswer()
            else:
                return self.AgentCollection[type-1].getOutput()


    def testQuestions(self, filename):
        file = open(filename, 'r')
        self.answers = []
        for line in file:
            self.myAgent.setInputText(line)
            self.answers.append(self.getAnswer(0))
        file.close()

    def outputAnswers(self, filename):
        file = open(filename, 'w')
        aString = ""
        for i in self.answers:
            aString += i + "\n"
        file.write(aString)
        file.close()

    def checkAnswers(self, filename):
        file = open(filename, 'r')
        counter = 0
        index = 0
        for line in file:
            if str(self.answers[index]) == line.replace('\n', '').lower():
                counter += 1
            index += 1
        file.close()
        return counter, index - counter


    def loadFile(self, file):
        self.AgentCollection[2].loadData(file)

    def saveFile(self, file):
        self.AgentCollection[2].saveData(file)
