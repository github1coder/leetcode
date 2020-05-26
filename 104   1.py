# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ma=0
        def dfs(node,deep):
            if not node:
                return 
            self.ma=max(self.ma,deep)
            dfs(node.left,deep+1)
            dfs(node.right,deep+1)
        dfs(root,1)
        return self.ma