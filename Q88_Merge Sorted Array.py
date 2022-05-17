class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # O(1)
        if n == 0:
            return None
        ans = [] 
        i = j = 0
        #O(min(m,n)), total is O(m+n)
        while(i<m and j < n):
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i < m:
            while(i<m):
                ans.append(nums1[i])
                i += 1
        elif(j < n):
            while(j < n):
                ans.append(nums2[j])
                j += 1
        #O(m+n)
        for k in range(len(ans)):
            nums1[k] = ans[k]
            
        return nums1
      #Total is 2 O(m+n)
