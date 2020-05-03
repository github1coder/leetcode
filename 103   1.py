# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        path=[]
        self.le=0
        def dfs(node,depth,sign):
            if node:a
                if depth+1 > self.le:
                    path.append([])
                    self.le+=1
                if sign==0:
                    path[depth].append(node.val)
                    dfs(node.left,depth+1,1)
                    dfs(node.right,depth+1,1)
                else:
                    path[depth].insert(0,node.val)
                    dfs(node.left,depth+1,0)
                    dfs(node.right,depth+1,0)
        dfs(root,0,0)
        return path