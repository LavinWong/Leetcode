class MinStack(object):

    def __init__(self):
        self.items = []
        self.min = 1e6

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.append(val)
        return self.items
        

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        x = self.items[-1]
        return x

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
