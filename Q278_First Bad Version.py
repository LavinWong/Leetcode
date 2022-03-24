# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 0, n
        if(n == 1):
            return n
        while(left<=right):
            mid = (left + right) // 2
            if(left == right):
                return mid
            state = isBadVersion(mid)
            if(state):
                ans = mid
                right = mid 
            else:
                left = mid + 1
        print(ans)
        return ans
