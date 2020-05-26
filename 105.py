# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorderleft:int,preorderright:int,inorderleft:int,inorderright:int):
            if preorderleft>preorderright:
                return None
            preorderroot=preorderleft
            inorderroot=index[preorder[preorderroot]]
            root=TreeNode(preorder[preorderroot])
            sizeleft=inorderroot-inorderleft
            root.left=build(preorderleft+1,preorderleft+sizeleft,inorderleft,inorderroot-1)
            root.right=build(preorderleft+sizeleft+1,preorderright,inorderroot+1,inorderright)
            return root
        n=len(preorder)
        index={el:i for i,el in enumerate(inorder)}
        return build(0,n-1,0,n-1)