# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        path=[]
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                path.append(node.val)
        dfs(root)
        return path