# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.s=0
        def dfs(node,su):
            if not node:
                return 
            node.val+=su
            dfs(node.left,node.val)
            dfs(node.right,node.val)
        dfs(root,0)
        def find(node,pre):
            if not node:
                return
            if node.val-pre==sum:
                self.s+=1
            find(node.left,pre)
            find(node.right,pre)
        def df(node):
            if not node:
                return 
            if node.val==sum:
                self.s+=1
            find(node.left,node.val)
            find(node.right,node.val)
            df(node.left)
            df(node.right)
        df(root)
        return self.s 