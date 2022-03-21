class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #First of all, we check is the list1 or list 2 is empty.
        if(len(nums1)==0 or len(nums2)==0):
            if(len(nums1)==0):
                if(len(nums2)%2==0):
                    return (nums2[len(nums2)/2]+nums2[(len(nums2)-1)/2])/2.0
                else:
                    return nums2[len(nums2)/2]
            elif(len(nums2)==0):
                if(len(nums1)%2==0):
                    return (nums1[len(nums1)/2]+nums1[(len(nums1)-1)/2])/2.0
                else:
                    return nums1[len(nums1)/2]
        
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2

        # -> binary search
        total_length = len(nums1) + len(nums2)
        
        partition_size = (total_length + 1) //2
        odd = total_length % 2
        
        low = 0 # -> min no. of elements I can take from nums1
        high = min(len(nums1), partition_size) # -> max no. of elements I can take from nums2
        
        while low <= high:
            cut_on_nums1 = (low + high)//2
            cut_on_nums2 = partition_size - cut_on_nums1
            
            if cut_on_nums1 == 0:
                nums1_leftmax = float('inf')*(-1)
            else:
                nums1_leftmax = nums1[cut_on_nums1-1]
                
            if cut_on_nums2 == 0:
                nums2_leftmax = float('inf')*(-1)

            else:
                nums2_leftmax = nums2[cut_on_nums2-1]
                
            if cut_on_nums1 == len(nums1):
                nums1_rightmin = float('inf')
            else:
                nums1_rightmin = nums1[cut_on_nums1]
            
            if cut_on_nums2 == len(nums2):
                nums2_rightmin = float('inf')
            else:
                nums2_rightmin = nums2[cut_on_nums2]
                
            if nums1_leftmax <= nums2_rightmin and nums2_leftmax <= nums1_rightmin:
                if odd:
                    return max(nums1_leftmax, nums2_leftmax)
                else:
                    return (max(nums1_leftmax, nums2_leftmax) + min(nums1_rightmin, nums2_rightmin))/2.0
            
            elif nums1_leftmax > nums2_rightmin:
                high = cut_on_nums1 - 1
            
            else:
                low = cut_on_nums1 + 1
        
        return 0
