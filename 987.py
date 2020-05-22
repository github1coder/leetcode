# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res=collections.defaultdict(list)
        
        def dfs(node,x,y):
            if not node:
                return 
            dfs(node.left,x-1,y-1)
            res[x].append((-y,node.val))
            dfs(node.right,x+1,y-1)
        dfs(root,0,0)
        keys=sorted(list(res.keys()))
        return [[i[1] for i in sorted(res[k])] for k in keys]
