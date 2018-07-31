class Node:
    # Node constructor
    def __init__(self, aWord):
        self.word = aWord
        self.relation = []

    # Add new word relation
    def addNew(self, aWord, point):
        self.relation.append([aWord, point])

    # Add new set of word relations
    def addNewSeq(self, aSeq):
        for i in aSeq:
            self.relation.append([i, 0])

    # Word string accessor
    def getWord(self):
        return self.word

    # List of relationship array accessor
    def getRelation(self):
        return self.relation

    # Calculate the point relationship of inputted words array
    def getPoint(self, aSeq):
        total = 0
        for i in aSeq:
            j = 0
            found = False
            while(not(found) and j < len(self.relation)):
                if i == self.relation[j][0]:
                    total += self.relation[j][1]
                    found = True
                j += 1
            if not(found):
                self.addNew(i, 0)
        return total

    # Get the point relationship of specific word
    def getPointWord(self, word):
        for i in self.relation:
            if i[0] == word:
                return i[1]
        return 0

    # Add a reward point to a specific word relationship
    def addReward(self, aWord, point):
        for i in range(len(self.relation)):
            if self.relation[i][0] == aWord:
                self.relation[i][1] += point
                if self.relation[i][1] > 5:
                    self.relation[i][1] = 5
                elif self.relation[i][1] < -5:
                    self.relation[i][1] = -5
                return True
        return False