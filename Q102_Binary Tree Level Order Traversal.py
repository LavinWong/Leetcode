# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def breadth_first_search(self, root, result, level):
		if root==None:
			return root
		if len(result) == level:
			result.append([])
		result[level].append(root.val)
		self.breadth_first_search(root.left,  result, level + 1)
		self.breadth_first_search(root.right, result, level + 1)
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
			return root
        result = []
        self.breadth_first_search(root, result, 0)
        return result
