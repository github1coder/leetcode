# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.mi=99999999
        self.pre=-9999999
        def back(root):
            if not root:
                return 
            back(root.left)
            self.mi=min(self.mi,root.val-self.pre)
            self.pre=root.val 
            back(root.right)
        back(root)
        return self.mi