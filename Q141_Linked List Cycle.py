# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        state = False
        h = set()
        while head:
            if head in h:
                state = True
                return state
            h.add(head)
            head = head.next
        return state
################################################
#Other way
class Solution:
    def hasCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast: return True
        return False
      
################################################
#Other way
class Solution:
    def hasCycle(self, head):
        D={}
        while head:
            if head in D: 
                return True
            D[head]=True
            head=head.next
        return False
