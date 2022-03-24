class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums)-1
        if(len(nums) == 1):
            return nums[right]
        while left <= right:
            mid = (left+right)//2
            if (mid!=len(nums)-1 and nums[mid]==nums[mid+1]): #comparing 1st appearence with next element
                mid += 1;#setting mid to 2nd appearence 
            if mid%2!=0:#searching right side of the array
                left = mid+1;
            else :
                if mid==0 or nums[mid-1]!=nums[mid]:# got the mid
                    return nums[mid]
                right = mid-2;# else search in left part of the arary
        
        
