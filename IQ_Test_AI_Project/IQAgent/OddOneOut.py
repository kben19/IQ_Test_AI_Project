import random

from IQAgent import Node, Hash
from IQAgent.Agent import Agent


# Odd one out class inherit Agent class
class OddOneOut(Agent):
    # Odd one out constructor
    def __init__(self, input = ""):
        Agent.__init__(self, input)
        self.wordList = Hash.Hash(1000)
        self.nodeList = []

    # Override method in Agent
    # Function that get the elements needed to solve the question
    def getSequence(self):
        # Generalized the input text
        temp = self.inputText.split(':')    # Split between the question and the words
        if len(temp) > 1:
            temp = temp[1].split(',')           # Get the odd one out words
            temp = [x.replace('.','') for x in temp]    # Remove .
            temp = [x.replace('?','') for x in temp]    # Remove ?
            temp = [x.replace('\n','') for x in temp]   # Remove newline
            temp = [x[1:] if x[0] == " " else x for x in temp]  # Remove the first blank space
            temp = [x.lower() for x in temp]            # Lowercase string
        else:
            temp = []
        return temp

    # Function that get the words of the questions from the wordList
    def makeNodeList(self):
        if len(self.sequence) != 0:
            for i in range(len(self.sequence)):
                temp = self.wordList.lookup(self.sequence[i].replace('_', ' '))
                if temp != -1:      # If the word is exist
                    self.nodeList.append(temp)
                if temp == -1:      # If the word is not exist
                    newNode = Node.Node(self.sequence[i])
                    newNode.addNewSeq(self.sequence[:i] + self.sequence[i+1:])
                    self.wordList.insert(newNode)
                    self.nodeList.append(newNode)

    # Override method in Agent
    # Function that solve the question and set the output
    # The function return the index of the odd one out words starting from 0 index
    def solve(self):
        index = -1
        point = 16       # Maximum point a node can have is 15
        decision = -1
        self.output = ""
        self.sequence = self.getSequence()  # Get the words
        self.nodeList = []                  # Reset the nodeList
        self.makeNodeList()                 # Get the words as nodes
        if len(self.sequence) != 0:
            startPoint = self.nodeList[0].getPoint(self.sequence[1:])
            change = True

            # Check if every words score if the same or not
            for i in range(1, len(self.nodeList)):
                if startPoint != self.nodeList[i].getPoint(self.sequence[:i] + self.sequence[i+1:]):
                    change = False
            # If the words score is the same then choose randomly
            if change:
                decision = random.randint(0, len(self.nodeList)-1)
            # Otherwise choose the lowest one
            else:
                for i in range(len(self.nodeList)):
                    if point > self.nodeList[i].getPoint(self.sequence[:i] + self.sequence[i+1:]):
                        point = self.nodeList[i].getPoint(self.sequence[:i] + self.sequence[i+1:])
                        index = i
                decision = index


            self.output = self.sequence[decision]
        return decision

    # Function that receives questions array and answers array for machine to learn
    def learning(self, questions, answers):
        for i in range(len(questions)):
            decision = -1
            while decision != answers[i]:
                self.setInputText(questions[i])
                decision = self.solve()
                self.reinforce(decision, answers[i])

    # Function that reinforce the reward of words relationship based on the decision feedback
    def reinforce(self, decision, correct):
        for i in range(len(self.nodeList)-1):
            for j in range(i+1, len(self.nodeList)):
                if i != decision and j != decision:
                    self.nodeList[i].addReward(self.nodeList[j].getWord(), 1 if decision == correct else -1)
                    self.nodeList[j].addReward(self.nodeList[i].getWord(), 1 if decision == correct else -1)
                else:
                    self.nodeList[i].addReward(self.nodeList[j].getWord(), -1 if decision == correct else 1)
                    self.nodeList[j].addReward(self.nodeList[i].getWord(), -1 if decision == correct else 1)

    # save the current knowledge to the output file
    def saveData(self, outputFile):
        file = open(outputFile, 'w')
        aString = ""
        for i in self.wordList.getHashList():
            if i != None:
                temp = i.getWord().replace(' ', '_')
                aString += temp + " "
                for j in i.getRelation():
                    aString += j[0].replace(' ', '_') + "|" + str(j[1]) + " "
                aString = aString[:len(aString)-1] + "\n"
        file.write(aString)
        file.close()

    # load the inputted knowledge file into the agent knowledge (overwrite)
    def loadData(self, inputFile):
        self.wordList = Hash.Hash(len(self.wordList))
        file = open(inputFile, 'r')
        for line in file:
            line = line[:len(line)-1]
            temp = line.split(" ")
            aNode = Node.Node(temp[0].replace('_', ' '))
            for j in range(1, len(temp)):
                relation = temp[j].replace('_', ' ').split('|')
                aNode.addNew(relation[0], int(relation[1]))
            self.wordList.insert(aNode)
        file.close()