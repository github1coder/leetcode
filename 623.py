# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d==1:
            new=TreeNode(v)
            new.left=root
            return new
        
        def op(i,node):
            if node==None:
                return
            if i==d-1:
                le=node.left
                ri=node.right
                newleft=TreeNode(v)
                newleft.left=le
                newright=TreeNode(v)
                newright.right=ri
                node.left=newleft
                node.right=newright
                return 
            op(i+1,node.left)
            op(i+1,node.right)
        
        op(1,root)
        return root
