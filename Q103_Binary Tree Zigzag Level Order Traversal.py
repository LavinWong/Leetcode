# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bfs(self, root, result, level):
        if root is None:
            return root
        if len(result) == level:
            result.append([])
        result[level].append(root.val)
        print(level)
        if(level %2 == 0):
            self.bfs(root.right,result,level+1)
            self.bfs(root.left,result,level+1)
        else:
            self.bfs(root.left,result,level+1)
            self.bfs(root.right,result,level+1)
        
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        result = []
        self.bfs(root,result,0)
        return result
####################################################################
class Solution:
    def zigzagLevelOrder(self, root):
        result, nodes, direction = [], [root], True
        if root != None:
            while len(nodes)>0:
                tempResult, childNodes = [], []
                while len(nodes)>0:
                    temp = nodes.pop()
                    tempResult.append(temp.val)
                    if direction:
                        childNodes.append(temp.left)
                        childNodes.append(temp.right)
                    else:
                        childNodes.append(temp.right)
                        childNodes.append(temp.left)
                result.append(tempResult)
                nodes = [node for node in childNodes if node!=None]
                direction = not direction
        return result
