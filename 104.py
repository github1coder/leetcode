# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ma=0
        if not root:
            return 0
        def dfs(root,high):
            if not root:
                return 0
            if dfs(root.left,high+1)+dfs(root.right,high+1)==0:
                self.ma=max(self.ma,high)
            return 1
        dfs(root,1)
        return self.ma