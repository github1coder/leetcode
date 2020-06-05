# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def reverse(node):
            if not node:
                return 
            node.left,node.right=node.right,node.left
            reverse(node.left)
            reverse(node.right)
        reverse(root)
        return root