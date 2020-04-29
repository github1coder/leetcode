# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.s=0
        self.l=L 
        self.r=R 
        def back(root):
            if not root:
                return
            if root.val>=self.l:
                back(root.left)
            if self.l<=root.val<=self.r :
                self.s+=root.val
            if root.val<=self.r:
                back(root.right)
            
        back(root)
        return self.s
        