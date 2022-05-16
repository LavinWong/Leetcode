class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.len = 0
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        instate = False
        if val not in self.list:
            instate = True
            self.list.append(val)
            self.len += 1
        return instate
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        rmstate = False
        if val in self.list:
            self.list.remove(val)
            rmstate = True
            self.len -= 1
        return rmstate
        

    def getRandom(self):
        """
        :rtype: int
        """
        if self.len < 1:
            return False
        else:
            return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
