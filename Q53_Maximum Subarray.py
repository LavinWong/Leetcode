class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return
        finalans = 0
        corrans = 0
        for i in nums:
            corrans = max(0,corrans+i)
            finalans = max(corrans,finalans)
        if(finalans == 0):
            return max(nums)
        return finalans
