# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p=p.val
        self.q=q.val
        def dfs(root):
            if root:
                if self.p<=root.val<=self.q or self.q<=root.val<=self.p:
                    return root
                if root.val < self.p and root.val < self.q:
                    return dfs(root.right)
                return dfs(root.left)
        return dfs(root)