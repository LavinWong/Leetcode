class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.list = [0]*size
        self.count = 0
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        index = self.count % self.size 
        self.total -= self.list[index]
        self.list[index] = val 
        self.total += val
        self.count += 1
        ans = self.total/float(min(self.count,self.size))
        return ans


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
