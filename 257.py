# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path=[]
        def dfs(node,s):
            if not node:
                return
            s+=str(node.val)
            if not node.left and not node.right:
                path.append(s)
            else:
                s+="->"
                dfs(node.left,s)
                dfs(node.right,s) 
        dfs(root,"")
        return path
        