# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path=[]
        def dfs(s,root):
            if not root:
                return
            s=s+str(root.val)
            if not root.left and not root.right:
                path.append(s)
                return
            else:
                s=s+"->"
            dfs(s,root.left)
            dfs(s,root.right)
            return
        dfs("",root)
        return path