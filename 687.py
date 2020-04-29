# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans=0
        def back(root):
            if not root: return 0
            lle=back(root.left)
            lri=back(root.right)
            la=ra=0
            if root.left and root.val==root.left.val:
                la=lle+1
            if root.right and root.val==root.right.val:
                ra=lri+1
            self.ans=max(self.ans,la+ra)
            return max(la,ra)
        back(root)
        return self.ans