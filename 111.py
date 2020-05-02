# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=collections.deque()
        queue.append([1,root])
        while queue:
            depth,cur=queue.popleft()
            if not cur.left and not cur.right:
                return depth
            if cur.left:
                queue.append([depth+1,cur.left])
            if cur.right:
                queue.append([depth+1,cur.right])
