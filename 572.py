# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def back(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return back(p.left,q.left) and back(p.right,q.right)
        def dfs(p,q):
            if p:
                if back(p,q):
                    return True
                return dfs(p.left,q) or dfs(p.right,q)
            else:
                return False
        return dfs(s,t)

