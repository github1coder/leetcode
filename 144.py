# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        path=[]
        def dfs(node):
            if node:
                path.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return path