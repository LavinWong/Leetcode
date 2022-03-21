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

        # We get the total length
        total_length = len(nums1) + len(nums2)
        
        #We get the number of elements we need
        partition_size = (total_length + 1) //2
        
        #Check it will be one or two.
        odd = total_length % 2
        
        low = 0 # -> min no. of elements I can take from nums1
        high = min(len(nums1), partition_size) # -> max no. of elements I can take from nums2
        
        while low <= high:
            #How many we will take from nums1.
            cut_on_nums1 = (low + high)//2
            
            #How many we will take from nums2.
            cut_on_nums2 = partition_size - cut_on_nums1
            
            #if i do not need any element from left nums1 part.
            if cut_on_nums1 == 0:
                nums1_leftmax = float('inf')*(-1)
            #I mark the maximum number is left of nums1.
            else:
                nums1_leftmax = nums1[cut_on_nums1-1]
            
            #if i do not need any element from left nums2 part.
            if cut_on_nums2 == 0:
                nums2_leftmax = float('inf')*(-1)
            #I mark the maximum number is left of nums2.
            else:
                nums2_leftmax = nums2[cut_on_nums2-1]
            
            #if i do not need any element from right nums1 part.
            if cut_on_nums1 == len(nums1):
                nums1_rightmin = float('inf')
            #I mark the minimum number is right of nums1.
            else:
                nums1_rightmin = nums1[cut_on_nums1]
            
            #if i do not need any element from right nums2 part.
            if cut_on_nums2 == len(nums2):
                nums2_rightmin = float('inf')
            #I mark the minimum number is right of nums2.
            else:
                nums2_rightmin = nums2[cut_on_nums2]
            # the middle number in the left part.   
            if nums1_leftmax <= nums2_rightmin and nums2_leftmax <= nums1_rightmin:
                if odd:
                    return max(nums1_leftmax, nums2_leftmax)
                else:
                    return (max(nums1_leftmax, nums2_leftmax) + min(nums1_rightmin, nums2_rightmin))/2.0
            #we will take less in left nums1 part and will make more in left nums2 part.
            elif nums1_leftmax > nums2_rightmin:
                high = cut_on_nums1 - 1
            #nums2_leftmax > nums1_rightmin, so we will make more in left nums1 part and take less in left nums2 part.
            else:
                low = cut_on_nums1 + 1
        
        return 0
