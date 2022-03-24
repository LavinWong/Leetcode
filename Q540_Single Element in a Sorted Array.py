class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums)-1
        if(len(nums) == 1):
            return nums[right]
        while left <= right:
            mid = (left+right)//2
            #we want to know the single element is in left part or right part.
            #comparing 1st appearence with next element
            #we just make this pair in left
            if (mid!=len(nums)-1 and nums[mid]==nums[mid+1]): 
                mid += 1;#setting mid to 2nd appearence
            #if in this case, the single part is in right part.
            if mid%2!=0:#searching right side of the array
                left = mid+1;
            #if in this case, the single part is in left part.
            else :
                if mid==0 or nums[mid-1]!=nums[mid]:# got the mid
                    return nums[mid]
                right = mid-2;# else search in left part of the arary
        
        
