# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.m=0
        def dfs(node,s):
            if not node :
                return
            s+=node.val
            if s==sum and not node.right and not node.left:
                self.m=1
                return
            dfs(node.left,s)
            dfs(node.right,s)
        dfs(root,0)
        return self.m==1