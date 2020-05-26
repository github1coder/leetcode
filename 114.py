# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        a=lambda root:[] if not root else [root.val]+a(root.left)+a(root.right)
        tl=lambda lst:TreeNode(lst[0],None,tl(lst[1:])) if lst else None
        tmp=a(root)
        root.left=None
        root.right=tl(tmp[1:])