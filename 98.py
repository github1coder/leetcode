# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        for i in range(len(res)):
            if i>0 and res[i]<=res[i-1]:
                return False
        return True