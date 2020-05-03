# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        path=[]
        self.le=0
        def dfs(node,depth):
            if node:
                if depth+1 > self.le:
                    path.append([])
                    self.le+=1
                path[depth].append(node.val)
                dfs(node.left,depth+1)
                dfs(node.right,depth+1)
        dfs(root,0)
        return path