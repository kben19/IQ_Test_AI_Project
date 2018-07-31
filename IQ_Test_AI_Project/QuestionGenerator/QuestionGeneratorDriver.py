from QuestionGenerator import QuestionGenerator

class QuestionGeneratorDriver():

    # Question Generator Driver constructor
    def __init__(self, anAgent):
        self.myAgent = anAgent
        self.myGenerator = QuestionGenerator.QuestionGenerator()

    # Agent accessor
    def setAgent(self, anAgent):
        self.myAgent = anAgent

    # Make the agent learn the samples
    def learnSamples(self, baseFile, categoryFile, categoryNum, totalLearn):
        if self.myAgent != None:
            categoryList = self.myGenerator.makeCategory(baseFile, categoryFile, categoryNum)
            self.myGenerator.learn(self.myAgent, baseFile, categoryList, totalLearn)

    # Test the agent with generated samples
    def testSamples(self, baseFile, categoryFile, categoryNum, totalTest):
        if self.myAgent != None:
            categoryList = self.myGenerator.makeCategory(baseFile, categoryFile, categoryNum)
            return self.myGenerator.testCases(self.myAgent, baseFile, categoryList, totalTest)

    # Generate the questions and answers and write it into the output file
    def outputQuestions(self, QuestionFile, AnswerFile, baseFile, categoryFile, catNum, totalNum, answerType):
        QFile = open(QuestionFile, 'w')
        AFile = open(AnswerFile, 'w')
        fBase = open(baseFile, 'r')
        baseList = fBase.read().split("\n")
        fBase.close()
        categoryList = self.myGenerator.makeCategory(baseFile, categoryFile, catNum)
        questions, answers = self.myGenerator.generateTestCases(baseList, categoryList, totalNum, answerType)

        questionString, answerString = "", ""
        for i in questions:
            questionString += i + "\n"
        for i in answers:
            answerString += i + "\n"

        QFile.write(questionString)
        AFile.write(answerString)
        QFile.close()
        AFile.close()