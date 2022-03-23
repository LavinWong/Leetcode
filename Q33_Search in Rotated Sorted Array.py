class Solution:
    def search(self, nums, target):
        
        
        #Going to be doing a Binary Search to find a O(log n) solution
        
        #initialize our left and right pointers
        left, right = 0, len(nums) - 1
        
        #We're going to keep running binary search until our pointers intersect
        while left <= right:
            
            #Our middle pointer
            mid = (left + right) // 2
            
            #If we find the number, just return the index
            if nums[mid] == target:
                return mid
            
            #We need to find out if we're in the left or right hand side of the array
            #Condition for being in the left side of the array
            if nums[left] <= nums[mid]:
                
                #If the target is larger than nums[mid] we need to look to the right
                if target > nums[mid]:
                    left = mid + 1
                    
                #If the target is smaller than nums[mid] and smaller than nums[left] we look right
                
                elif target < nums[mid] and target < nums[left]:
                    left = mid + 1
                
                #Else we look left
                else:
                    right = mid - 1
                    
            #Condition for being in the right side of the array
            else:
                #If the target is smaller than nums[mid] we look left
                if target < nums[mid]:
                    right = mid - 1
                
                #If the targer is larger than nums[mid] and larger than nums[right] we look
                #left
                elif target > nums[mid] and target > nums[right]:
                    right = mid - 1
                
                #Else look right
                else:
                    left = mid + 1
                    
        #If we never find anything we just return -1
        return -1
