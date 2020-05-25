# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if not node1:
                return False
            if not node2:
                return False
            if node1.val!=node2.val:
                return False
            return dfs(node1.left,node2.right) and dfs(node1.right,node2.left)
        return dfs(root,root)