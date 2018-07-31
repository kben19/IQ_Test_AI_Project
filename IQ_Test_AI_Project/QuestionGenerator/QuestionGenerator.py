import random

class QuestionGenerator():

    def __init__(self):
        pass

    # Generate category list which consist of list of list
    # The list consist of arrays that each array represent a words in the same category
    def makeCategory(self, baseFile, categoryFile, categoryNum):
        fBase = open(baseFile, 'r')
        fcategory = open(categoryFile, 'r')
        categoryOutput = []

        for i in range(categoryNum):
            categoryOutput.append([])

        baseList = fBase.read().split("\n")
        categoryList = []
        for line in fcategory:
            categoryList.append([int(x) for x in line.split()])
        fBase.close()
        fcategory.close()

        for i in range(len(baseList)):
            categoryOutput[categoryList[i][0]-1].append(i)

        return categoryOutput

    # Make the agent learn the generated samples
    def learn(self, anAgent, fileBase, categoryList, totalLearn):
        fBase = open(fileBase, 'r')
        baseList = fBase.read().split("\n")

        questions, answers = self.generateTestCases(baseList, categoryList, totalLearn, 0)
        anAgent.learning(questions, answers)


    # Test the agent knowledge with a given questions list and return the total of wrong answers
    def testCases(self, anAgent, baseFile, categoryList, totalNum):
        fBase = open(baseFile, 'r')
        baseList = fBase.read().split("\n")

        questions, answers = self.generateTestCases(baseList, categoryList, totalNum, 0)

        if len(questions) == len(answers):
            count = 0
            for i in range(len(questions)):
                anAgent.setInputText(questions[i])
                if answers[i] != (anAgent.solve()):
                    count += 1
            return count

    # Generate the test cases based from the base list and its category
    def generateTestCases(self, baseList, categoryList, aNum, answerType):
        questions = []
        answers = []
        for i in range(aNum):
            index = random.randint(0, len(categoryList)-1)
            indexDiff = random.randint(0, len(categoryList)-1)
            index1 = random.randint(0, len(categoryList[index])-1)
            index2 = random.randint(0, len(categoryList[index])-1)
            index3 = random.randint(0, len(categoryList[index])-1)
            while(index2 == index1):
                index2 = random.randint(0, len(categoryList[index])-1)
            while index3 == index1 or index3 == index2:
                index3 = random.randint(0, len(categoryList[index])-1)
            while indexDiff == index:
                indexDiff = random.randint(0, len(categoryList)-1)

            myList = [baseList[categoryList[index][index1]], baseList[categoryList[index][index2]], baseList[categoryList[index][index3]]]
            num = random.randint(0, 3)
            index2 = categoryList[indexDiff][random.randint(0, len(categoryList[indexDiff])-1)]
            myList.insert(num, baseList[index2])

            questions.append( "Odd One Out: " + str(myList)[ 1:len(str(myList))-1 ].replace("'", "") )
            if answerType == 0:
                answers.append(num)
            elif answerType == 1:
                answers.append(myList[num])
        return questions, answers