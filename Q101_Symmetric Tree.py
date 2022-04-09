# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        def compareSub(left_child, right_child):
            #If both is None. return true
            if left_child == None and right_child == None:
                return True
            #If one of is None just return false.
            if left_child == None or right_child == None:
                return False
            #if two child value is not equal, return false.
            if left_child.val != right_child.val:
                return False
            return compareSub(left_child.left, right_child.right) and compareSub(left_child.right, right_child.left)
        return compareSub(root, root)
