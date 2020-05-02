# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.m=1
        def dfs(node):
            if not node :
                return 0
            le=dfs(node.left)
            ri=dfs(node.right)
            if abs(le-ri)>1:
                self.m=0
            return 1+max(le,ri)
        dfs(root)
        return self.m==1