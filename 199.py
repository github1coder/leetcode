# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        num=[]
        def dfs(node,depth):
            if not node:
                return
            if depth+1>len(num):
                num.append(node.val)
            else:
                num[depth]=node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return num
            