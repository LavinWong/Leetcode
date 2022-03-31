class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0
        self.state = 0

    def next(self):
        """
        :rtype: int
        """
        if(self.index1 < len(self.v1) and self.index2 < len(self.v2)):
            if self.state == 0:
                self.index1 += 1
                self.state = 1 - self.state
                return self.v1[self.index1 - 1]
            else:
                self.index2 += 1
                self.state = 1 - self.state
                return self.v2[self.index2 - 1]
            
        elif(self.index1 == len(self.v1) and self.index2 < len(self.v2)):
            self.index2 += 1
            return self.v2[self.index2 - 1]
        
        elif(self.index2 == len(self.v2) and self.index1 < len(self.v1)):
            self.index1 += 1
            return self.v1[self.index1 - 1]
        else:
            return None
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index1<len(self.v1) or self.index2<len(self.v2):
            return True
        else:
            return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
