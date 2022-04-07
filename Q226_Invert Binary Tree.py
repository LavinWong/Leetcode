# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        new_tree = TreeNode(root.val)
        new_tree.left = self.invertTree(root.right)
        new_tree.right = self.invertTree(root.left)
        return new_tree
