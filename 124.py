# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ma=-99999999
        def dfs(node):
            if not node:
                return 0
            le=dfs(node.left)
            ri=dfs(node.right)
            t=node.val
            if le>0:
                t+=le
            if ri>0:
                t+=ri
            self.ma=max(self.ma,t)
            t=node.val
            m=max(le,ri)
            if m>0:
                t+=m
            return t
        dfs(root)
        return self.ma