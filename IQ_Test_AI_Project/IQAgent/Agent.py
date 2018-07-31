class Agent:
    # Agent Constructor
    def __init__(self, input = ""):
        self.inputText = input
        self.questionType = 0
        self.sequence = []
        self.multipleChoice = []
        self.output = None

    # input text mutator
    def setInputText(self, input):
        self.inputText = input

    # input text accessor
    def getInputText(self):
        return self.inputText

    # output accessor
    def getOutput(self):
        return self.output

    # Parse the input text question and determine the type of the question
    # Return 1 if number problem, 2 if direction problem, 3 if odd one out problem
    def checkType(self):
        self.questionType = 0
        if self.inputText != "":
            # Generalized  the input text
            temp = self.inputText.replace(',', '')
            temp = temp.replace('.', '')
            temp = temp.replace('?', '')
            temp = temp.replace(':', '')
            temp = temp.replace('\n', ' ')

            textArray = [x.lower() for x in temp.split(" ")]    # Convert the string into array
            questionTypeScore = [0, 0, 0]

            # Search for keywords representatives of each problem type
            for i in textArray:
                if i == "what" or i == "insert" or i == "which" or i == "next":
                    questionTypeScore[0] += 1
                elif i == "sequence" or i == "series" or i == "digit" or i == "number":
                    questionTypeScore[0] += 1
                elif i == "left" or i == "right" or i == "up" or i == "down" or i == "south" or i == "west" or i == "north" or i == "east":
                    questionTypeScore[1] += 1
                elif i == "not" or i == "belong" or i == "odd" or i == "one" or i == "out":
                    questionTypeScore[2] += 1

            # Determine the question type based on keywords count
            if questionTypeScore[0] >= 2:
                self.questionType = 1
            elif questionTypeScore[2] >= 2:
                self.questionType = 3
            elif questionTypeScore[1] > 1:
                self.questionType = 2
        return self.questionType

    # Function that parse the input text and get the multiple choices array if any
    def getMultipleChoice(self):
        self.multipleChoice = []
        if self.inputText != "":
            found = False
            index = 0
            temp = self.inputText.replace('\n', ' ')
            textArray = [x.lower() for x in temp.split()]
            aString = ""

            # Parse the string and check the multiple choices existence
            for i in range(len(textArray)):
                # Check if the multiple choice exist by checking the first 2 letter
                if (textArray[i][0] == "a" or textArray[i][0] == "b" or textArray[i][0] == "c" or textArray[i][0] == "d") and \
                        (textArray[i][1] == "." or textArray[i][1] == "," or textArray[i][1] == ")"):

                    found = True
                    if i - index == 1:  # If the multiple choice string is connected with the choice
                            aString = textArray[index][2:] + " "
                    if aString != "":   # add the previous multiple choice
                        # if i - index > 1:   # If the multiple choice string consist
                        aString = aString[:len(aString)-1]
                        self.multipleChoice.append(aString)
                    index = i
                    aString = ""
                elif found: # if the multiple choice exist
                    aString += textArray[i] + " "
            # If the multiple choices exist in the question then add the last choice
            if found:
                if index == len(textArray)-1:
                    aString= textArray[index][2:] + " "
                aString = aString[:len(aString)-1]
                self.multipleChoice.append(aString)
                for i in range(len(self.inputText)-1, -1, -1):
                    if self.inputText[i] == "a":
                        if self.inputText[i+1] == "." or self.inputText[i+1] == "," or self.inputText[i+1] == ")":
                            if self.inputText[i-1] == "\n":
                                i -= 1
                            self.inputText = self.inputText[:i]
                            break

    # Function that match the answer of the question with the multiple choices
    def getAnswer(self):
        if len(self.multipleChoice) != 0:
            self.solve()
            ans = str(self.output)
            for i in range(len(self.multipleChoice)):
                if self.multipleChoice[i] == ans:
                    return i
        return -1

    # Abstract method getSequence()
    def getSequence(self):
        pass

    # Abstract method Solve()
    def solve(self):
        pass
