class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=0
        b=0
        c=0
        for i in nums:
            if(i==0):
                a+=1
            elif(i==1):
                b+=1
            else:
                c+=1
        for i in range(a):
            nums[i]=0
        for i in range(b):
            nums[i+a]=1
        for i in range(c):
            nums[i+a+b]=2
