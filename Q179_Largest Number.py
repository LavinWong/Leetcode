class Solution(object):
    def compare(self, n1, n2):
		if  str(n1) + str(n2) > str(n2) + str(n1):
			return 1
		elif str(n1) + str(n2) < str(n2) + str(n1):
			return -1
		else:
			return 0
        
    def quickSort(self, nums):
		L = len(nums)
		if L <= 1:
			return nums

		p = nums[L//2]

		gt=[v for v in nums if self.compare(v,p)==1]
		eq=[v for v in nums if self.compare(v,p)==0]
		lt=[v for v in nums if self.compare(v,p)==-1]

		return self.quickSort(gt) + eq + self.quickSort(lt)
   
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        temp = self.quickSort(nums)
        return str(int("".join(map(str, temp)))) 
