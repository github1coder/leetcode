# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res=[]
        def op(root):
            if not root:
                return
            op(root.left)
            res.append(root.val)
            op(root.right)
        op(root)
        return res[k-1]