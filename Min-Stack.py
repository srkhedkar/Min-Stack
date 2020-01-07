class MinStack:
    # @param x, an integer
    def __init__(self):
        self.min = []
        self.dList = []
    
    def push(self, x):
        self.dList.append(x)

        if not self.min:
            self.min.append(x)
        elif (self.min[-1] > x):
            self.min.append(x)

    # @return nothing
    def pop(self):
        if not self.dList:
            return -1
        else:
            node = self.dList.pop()
            if node == self.min[-1]:
                self.min.pop()     
            
            new_list = self.dList.copy()
            self.dList = new_list

            return node

    # @return an integer
    def top(self):
        if not self.dList:
            return -1
        else:
            return self.dList[-1]

    # @return an integer
    def getMin(self):
        if not self.min:
            return -1
        else:
            return self.min[-1]