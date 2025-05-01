# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def getDepth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
                
            return depth
        
        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)
        
        if leftDepth == rightDepth: 
            return (1 << leftDepth) + self.countNodes(root.right)
        else:
            return (1 << rightDepth) + self.countNodes(root.left)        