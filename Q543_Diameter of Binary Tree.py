# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #if it is empty, just return 0
        if root is None :
            return 0
        #Set max equal to 0
        self.max_diameter = 0
        def dfs(root):
            #when it in the leaf.
            if not root:
                return 0
            #get the left adn right is exist or not
            left = dfs(root.left)
            right = dfs(root.right)
            self.max_diameter = max(left + right,self.max_diameter)
            return 1 + max(left,right)
    
        res = dfs(root)
        return self.max_diameter
