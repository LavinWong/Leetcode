class MyStack(object):

    def __init__(self):
        self.items = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x:
            self.items.append(x)
        return self.items
        
        

    def pop(self):
        """
        :rtype: int
        """
        x = self.items[-1]
        self.items.pop(-1)
        return x
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.items):
            return False
        else:
            return True
        
