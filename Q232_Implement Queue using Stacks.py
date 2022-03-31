class MyQueue(object):

    def __init__(self):
        self.list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        s = self.list[0]
        del self.list[0]
        return s
        

    def peek(self):
        """
        :rtype: int
        """
        return self.list[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.list):
            return False
        else:
            return True
        
