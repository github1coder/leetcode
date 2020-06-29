# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(node1,node2):
            if not node1:
                return node2
            if not node2:
                return node1
            node1.val+=node2.val
            node1.left=dfs(node1.left,node2.left)
            node1.right=dfs(node1.right,node2.right)
            return node1
        t1=dfs(t1,t2)
        return t1