class Hash():
    # Hash class constructor
    def __init__(self, listSize):
        self.tableSize = listSize
        self.hashList = [None] * self.tableSize
        self.prime = self.tableSize
        self.size = 0
        while not self.isPrime(self.prime):     # Generate prime number by finding the nearest prime number from table size
            self.prime += 1

    # Hash class length function
    def __len__(self):
        return self.tableSize

    # Hash list accessor
    def getHashList(self):
        return self.hashList

    # Generate hashing index number for hash table from string
    def hash_function(self, string):
        hashNumber = 0
        for i in list(string):
            hashNumber = (hashNumber * self.prime + ord(i))     # hash = ((a[0]) * prime + a[1]) ... * prime + a[n-1])
        return hashNumber % self.tableSize      # Keep the hash number generated by hash_function in table size range

    # Insert a string into the hash table using hash function
    def insert(self, item):
        index = self.hash_function(item.getWord())
        if self.hashList[index] is None:        # add item for the first time in hash table
            self.hashList[index] = item
        else:
            n = 1
            probing = (index + n) % self.tableSize
            n += 1

            while self.hashList[probing] is not None:   # Quadratic probing loop until it founds a free space
                probing = (probing + (n * n)) % self.tableSize      # Collision resolution by using quadratic probing
                n += 1
            self.hashList[probing] = item

        # Resize the hash table if the table is almost full
        self.size += 1
        if self.size > self.tableSize * 0.9:
            self.resize()

    # Return the value of the string in hash table
    def lookup(self, aString):
        n = 1
        index = self.hash_function(aString)
        probing = (index + n) % self.tableSize
        n += 1
        if self.hashList[index] is None:
            return -1
        elif self.hashList[index].getWord() == aString:
            return self.hashList[index]
        while self.hashList[probing] is not None:
            if self.hashList[probing].getWord() == aString:
                return self.hashList[probing]
            probing = (probing + (n * n)) % self.tableSize
            n += 1
        return -1

    # Delete the item in the hash table
    def delete(self, item):
        n =1
        index = self.hash_function(item.getWord())
        probing = (index + n) % self.tableSize
        n += 1
        if self.hashList[index] is None:
            return -1
        elif self.hashList[index].getWord() == item.getWord():
            self.hashList[index] = None
        while self.hashList[probing] is not None:
            if self.hashList[probing].getWord() == item.getWord():
                self.hashList[probing] = None
                break
            probing = (probing + (n * n)) % self.tableSize
            n += 1
        self.size -= 1
        return -1

    # Resize the table size by multiplying the current table size by 2
    # Redetermined the prime number used by the hash_function
    def resize(self):
        tempList = self.hashList
        self.__init__(self.tableSize * 2)
        for i in tempList:
            if i is not None:
                self.insert(i)      # Reinsert all the item of the hash table into the new resized table

    # Return true if the inputted number is prime, otherwise return false
    def isPrime(self, number):
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                return False
        return True