# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        elelist=[]
        #First of all, we keep all the elements in the one list.
        for i in lists:
            k=i
            while k:
                elelist.append(k.val)
                k=k.next
        #sort the list
        elelist.sort()
        #We creat the new list node and add the element which in the elementlist one by one
        p=ListNode(-1,None)
        q=p
        for i in range(len(elelist)):
            temp=ListNode(elelist[i],None)
            p.next=temp
            p=p.next
        return q.next
