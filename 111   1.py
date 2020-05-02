# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.mi=999999
        def bfs(node,depth):
            if not node:
                return 0
            l=bfs(node.left,depth+1)
            r=bfs(node.right,depth+1)
            if l+r==0:
                self.mi=min(self.mi,depth)
            return 1
        bfs(root,1)
        return self.mi