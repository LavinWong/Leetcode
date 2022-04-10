# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def compareSub(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            if (root1.left and root2.left and root1.left.val == root2.left.val) or (root1.right and root2.right and root1.right.val == root2.right.val):
                return compareSub(root1.left, root2.left) and compareSub(root1.right, root2.right)
            else:
                return compareSub(root1.left, root2.right) and compareSub(root2.left, root1.right)
            
        return compareSub(root1, root2)
            
