class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = -1
        for i in nums:
            x = target - i
            a=a+1
            b = -1
            for j in nums:
                b=b+1
                if x == j and a != b:                 
                    return a,b
