# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.s=0
        def dfs(node,sign):
            if node:
                if not node.left and not node.right and sign==1:
                    self.s+=node.val
                    return
                dfs(node.left,1)
                dfs(node.right,0)
        dfs(root,0)
        return self.s