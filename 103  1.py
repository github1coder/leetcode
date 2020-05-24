# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        def dfs(node,index):
            if not node:
                return 0
            if index+1>len(res):
                res.append([])
            if index%2==0:
                res[index].append(node.val)
            else:
                res[index].insert(0,node.val)
            dfs(node.left,index+1)
            dfs(node.right,index+1)
        dfs(root,0)
        return res