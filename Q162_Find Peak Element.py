class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0, len(nums)-1
        if(len(nums) == 1):
            return right
        while(left <= right):
            ans = -1
            mid = (right + left) // 2
            if(left == right):
                return mid
            if (nums[mid] > nums[mid+1] and nums[mid-1] < nums[mid]):
                return mid
            elif(nums[mid] < nums[mid+1]):
                left += 1 
            else:
                right -= 1
                
        
        return ans
