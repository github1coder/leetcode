# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path=[]
        def find(node,res,sum):
            if not node:
                return
            sum-=node.val
            if sum==0 and not node.left and not node.right:
                path.append(res+[node.val])
            find(node.left,res+[node.val],sum)
            find(node.right,res+[node.val],sum)
        find(root,[],sum)
        return path