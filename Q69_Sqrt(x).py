class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        root = x/2
        rep = 0.00001
        while(root - x / root > rep):
            root = 0.5*(root + x / root)
        return int(root)
