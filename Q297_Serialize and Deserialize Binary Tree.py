# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:
    def serialize(self, root):
        ans = ""
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if not node:
                ans += str(None) + " "
                continue
                
            ans += str(node.val) + " "
            q.append(node.left)
            q.append(node.right)
            
        return ans

    def deserialize(self, data):
        data = data.split()
        data = map(
            lambda val: TreeNode(int(val)) if val != 'None' else None, 
            data
        )
        data = deque(data)
        
        root = data.popleft()
        
        q = deque([root])
        
        while data:
            node = q.popleft()
            if not node:
                continue
            
            node.left = data.popleft()
            node.right = data.popleft()
            
            q.append(node.left)
            q.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
