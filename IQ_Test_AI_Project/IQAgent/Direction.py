from IQAgent.Agent import Agent
import math

class Direction(Agent):

    def __init__(self, input = ""):
        Agent.__init__(self, input)
        self.direction = []

    # Get the direction and distance data in the question
    def getSequence(self):
        self.direction = []
        self.sequence = []
        directionName = ["east", "south", "west", "north", "left", "right"]
        self.inputText = self.inputText.replace(',', '')
        self.inputText = self.inputText.replace('.', '')
        tempList = [x.lower() for x in self.inputText.split()]
        index = 0
        for i in tempList:
            if self.containItem(directionName, i):
                self.direction.append(i)
            elif i.isdigit():
                self.sequence.append(int(i))

    # Solve the direction problem
    def solve(self):
        x = 0
        y = 0
        prev = ""
        self.getSequence()
        for i in range(len(self.sequence)):
            if self.direction[i] == "east"\
                    or (self.direction[i] == "left" and prev == "south")\
                    or (self.direction[i] == "right" and prev == "north"):
                x += self.sequence[i]
                prev = "east"
            elif self.direction[i] == "south"\
                    or (self.direction[i] == "left" and prev == "west")\
                    or (self.direction[i] == "right" and prev == "east"):
                y -= self.sequence[i]
                prev = "south"
            elif self.direction[i] == "west"\
                    or (self.direction[i] == "left" and prev == "north")\
                    or (self.direction[i] == "right" and prev == "south"):
                x -= self.sequence[i]
                prev = "west"
            elif self.direction[i] == "north"\
                    or (self.direction[i] == "left" and prev == "east")\
                    or (self.direction[i] == "right" and prev == "west"):
                y += self.sequence[i]
                prev = "north"
        distance = math.sqrt(x**2 + y**2)
        dir = ""
        if y > 0:
            dir += "north "
        elif y < 0:
            dir += "south "
        if x > 0:
            dir += "east "
        elif x < 0:
            dir += "west "
        dir = dir[:len(dir)-1]

        self.output = str(distance) + " " + dir

    # Function that check if an item exist inside a list
    def containItem(self, aList, item):
        for i in aList:
            if item == i:
                return True
        return False