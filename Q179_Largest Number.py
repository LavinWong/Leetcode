class Solution(object):
    def compare(self, n1, n2):
	#I check the two strings and return the state.
	if  str(n1) + str(n2) > str(n2) + str(n1):
		return 1
	elif str(n1) + str(n2) < str(n2) + str(n1):
		return -1
	else:
		return 0
        
    def quickSort(self, nums):
	L = len(nums)
	#If just one element in the list, return it.
	if L <= 1:
		return nums

	p = nums[L//2]
	#input [10,2,8,9,0], p=[8]
	#I put the number large than mid number in gt list. [9]
	gt=[v for v in nums if self.compare(v,p)==1]
	#I put the number equal to mid number in eq list. [8]
	eq=[v for v in nums if self.compare(v,p)==0]
	#I put the number less than mid number in lt list. [10,2,0]
	lt=[v for v in nums if self.compare(v,p)==-1]

	return self.quickSort(gt) + eq + self.quickSort(lt)
   
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        temp = self.quickSort(nums)
        return str(int("".join(map(str, temp)))) 
