# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        temp = head
        while head:
            n += 1
            head = head.next
        i = n/2 +1
        if(n%2 == 0):
            x = n-i+1
        else:
            x= n-i
        print(i,n,x)
        while x > 0:
            x -= 1
            temp = temp.next
            
        return temp
