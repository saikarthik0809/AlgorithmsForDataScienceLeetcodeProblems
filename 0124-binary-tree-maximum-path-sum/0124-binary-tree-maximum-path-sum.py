# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            
            # dont take LMP if it is negative
            leftMaxPath = max(helper(node.left), 0)

            # dont take RMP if it is negative
            rightMaxPath = max(helper(node.right), 0)

            maxIfNodeIsRoot = node.val + leftMaxPath + rightMaxPath
            self.maxSum = max(self.maxSum, maxIfNodeIsRoot)
            return node.val + max(leftMaxPath, rightMaxPath)
        
        self.maxSum = float('-inf')
        helper(root)
        return self.maxSum