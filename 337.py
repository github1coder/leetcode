# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        def func(root):
            if not root:
                return 0,0
            leftnotdo,leftdo=func(root.left)
            rightnotdo,rightdo=func(root.right)

            return max(leftnotdo,leftdo)+max(rightnotdo,rightdo),leftnotdo+rightnotdo+root.val
        return max(func(root))