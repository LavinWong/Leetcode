class Solution(object):
    
    def binarysearch(self, arr, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if target > arr[mid]: 
              left = mid + 1
            else: 
              right = mid - 1
        #so we will get first element which  equal to target.
        return left
        
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                #I find the target and the the next large than target element.
                return self.binarysearch(nums,left,mid,target), self.findPos(nums,mid,right,target+1) - 1
            if target > nums[mid]: 
              left = mid + 1
            else: 
              right = mid - 1
        return [-1,-1]
