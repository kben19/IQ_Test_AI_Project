from IQAgent.Agent import Agent
import math

class Number(Agent):
    # Get the number sequence data from the question
    def getSequence(self):
        seqList = []
        tempList = self.inputText.replace(',', '')
        tempList = tempList.replace('.', '')
        tempList = tempList.replace('?', '')
        tempList = tempList.split()

        for i in range(len(tempList)-1):
            # If the current word and next word are number
            if tempList[i].isdigit() and tempList[i+1].isdigit():
                if len(seqList) == 0:   # Add the first digit of the sequence
                    seqList.append(int(tempList[i]))
                seqList.append(int(tempList[i+1]))

        return seqList

    # Solve the inputted question text by predicting the pattern and generate the next number
    def solve(self):
        self.sequence = self.getSequence()
        diffList = []
        self.output = ""
        for i in range(len(self.sequence)-1):
            diffList.append(self.sequence[i+1] - self.sequence[i])

        funcList = [self.multiplication(diffList), self.prime(), self.secondDifferences(diffList), self.twoDifferences(diffList),
                    self.power(self.sequence), self.fixedPower(), self.fibonnaci()]
        for i in funcList:
            if i[0]:
                self.output = i[1]
                return self.output
        return self.output

    # Predict the multiplication sequence pattern
    def multiplication(self, diffList):
        change = False
        tempNum = None
        for i in range(len(diffList) - 1):
            if diffList[i] != diffList[i+1]:
                change = True

        if not(change):
            tempNum = self.sequence[len(self.sequence)-1] + diffList[0]

        return [not change, tempNum]

    def secondDifferences(self, diffList):
        diffList2 = []
        tempNum = None
        if not(self.multiplication(diffList)):
            for i in range(len(diffList) - 1):
                diffList2.append(diffList[i+1] - diffList[i])
            if self.multiplication(diffList2):
                tempNum = self.sequence[len(self.sequence)-1] + diffList2[0] + diffList[len(diffList)-1]
                return [True, tempNum]
            elif self.power(diffList):
                tempNum = self.sequence[len(self.sequence)-1] + diffList2[1]/diffList2[0] * diffList[len(diffList)-1]
                return [True, tempNum]
            else:
                return [False, tempNum]
        return [False, tempNum]

    # Predict the sequence pattern that has different differences for even and odd index
    def twoDifferences(self, diffList):
        tempNum = None
        for i in range(len(diffList)-2):
            if diffList[i] != diffList[i+2]:
                return [False, tempNum]

        tempNum = self.sequence[len(self.sequence)-1] + (diffList[0 if len(diffList) % 2 == 0 else 1])
        return [True, tempNum]

    # Predict the power sequence pattern
    def power(self, aList):
        tempNum = None
        for i in range(len(aList)-1):
            if aList[i] > aList[i+1]:
                return [False, tempNum]

        basePower = aList[1] / aList[0]
        for i in range(1, len(aList)-1):
            if aList[i+1] / aList[i] != basePower:
                return [False, tempNum]

        tempNum = aList[len(aList)-1] * basePower
        return [True, tempNum]

    # Predict the power sequence where the power is the constant
    def fixedPower(self):
        j = 2   # Start by 2 to prevent zero division error
        if self.sequence[0] == 1:   # Remove number 1 in the sequence
            self.sequence.remove(1)
        match = False
        tempNum = None
        while j < 100:  # limitations of 100 arithmetic sequence
            num1 = self.sequence[0] % j
            num2 = self.sequence[1] % (j+1)
            # Base check of the arithmetic sequence
            if num1 == 0 and num2 == 0:
                match = True
                # Check if all sequence number are divisible by respective arithmetic sequence number
                for i in range(len(self.sequence)-1):
                    # If the arithmetic sequence do not match with the sequence number
                    if self.sequence[i] % (j+i) != 0 or self.sequence[i+1] % (j+1+i) != 0:
                        match = False
                        break
            if match:
                break
            j += 1

        for i in range(len(self.sequence)-1):
            power1 = int(math.log(self.sequence[i], j+i))
            power2 = int(math.log(self.sequence[i+1], j+1+i))
            if power1 != power2:    # Second check of power pattern using logarithm function
                return [False, tempNum]
        tempNum = (len(self.sequence) + j) ** power1
        return [True, tempNum]

    # Predict the fibonnaci sequence pattern
    def fibonnaci(self):
        pattern = True
        tempNum = None
        for i in range(len(self.sequence)-1, 1, -1):
            if self.sequence[i] != self.sequence[i-1] + self.sequence[i-2]:
                pattern = False

        if pattern:
            tempNum = self.sequence[len(self.sequence)-1] + self.sequence[len(self.sequence)-2]
        return [pattern, tempNum]

    # Predict the prime sequence pattern
    def prime(self):
        tempNum = None
        for i in self.sequence:
            if not(self.isPrime(i)): # Check if the number is prime
                return [False, tempNum]
        if (self.sequence[len(self.sequence)-1] + 1) % 6 == 0:
            output1 = self.sequence[len(self.sequence)-1] + 2
        elif (self.sequence[len(self.sequence)-1] - 1) % 6 == 0:
            output1 = self.sequence[len(self.sequence)-1] + 4
        output2 = self.sequence[len(self.sequence)-1] + 6
        tempNum = output1 if self.isPrime(output1) else output2
        return [True, tempNum]

    # Function that check the primality test of the inputted number
    def isPrime(self, num):
        if num % 2 != 0 and num % 3 != 0:
            n = int(math.sqrt(num))
            j = 1
            while 6*j - 1 <= n or 6*j +1 <= n:
                if 6*j - 1 <= n and num % (6*j-1) == 0:
                    return False
                if 6*j + 1 <= n and num % (6*j+1) == 0:
                    return False
                j += 1
        else:
            return False
        return True