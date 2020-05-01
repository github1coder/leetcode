# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        def bfs(node,depth):
            if not node: return
            if depth+1>len(res):
                res.append([])
            if depth % 2==0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0,node.val)
            bfs(node.left,depth+1)
            bfs(node.right,depth+1)
        bfs(root,0)
        return res