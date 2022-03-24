# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

#First of all, we find the peak in the mountain array, once we get it, we do the search in two steps. First we search the first array and if we do not find it
#we search the second part.
#otherwise, we return -1.
class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        start = 0
        end = mountain_arr.length() - 1
        endCopy = end
    
        #O(logn) time and O(1) space
        def findpeak(start,end):
            while start < end:
                mid = (start+end)//2
                midVal = mountain_arr.get(mid)
                midValPlusOne = mountain_arr.get(mid+1)
            #climbing mountain
                if midVal< midValPlusOne:
                    start = mid + 1

            #going down the mountain
                elif midVal > midValPlusOne:
                    end = mid
            return start
    
        peak = findpeak(start,end)
    
        def find(start,end,isAscending):
            ans = -1
            while start <= end:
                mid = (start+end)//2
                midVal = mountain_arr.get(mid)

                if midVal == target:
                    return mid

                if midVal<target:
                    if isAscending: 
                        start = mid + 1
                    else: 
                        end = mid - 1

                elif midVal>target:
                    if isAscending: 
                        end = mid - 1
                    else: 
                        start = mid + 1
            return ans
    
        #O(logn)
        ans = find(0,peak,True)
        if ans == -1:
            ans = find(peak,endCopy,False) #O(logn)
        return ans
        
