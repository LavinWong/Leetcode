# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ansList = ListNode()
        curr = ansList
        carry = 0
        while(l1 or l2 or carry):
            
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            c = a + b + carry
            carry = 1 if c >= 10 else 0
            digit = c % 10
            
            curr.next = ListNode(digit)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return ansList.next
