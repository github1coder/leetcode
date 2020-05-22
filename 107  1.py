# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        def dfs(node,index):
            if not node:
                return
            if index==len(res):
                res.insert(0,[])
            res[-index-1].append(node.val)
            dfs(node.left,index+1)
            dfs(node.right,index+1)
        dfs(root,0)
        return res