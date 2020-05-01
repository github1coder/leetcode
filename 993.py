# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        an=[[0,0],[0,0]]
        self.i=0
        self.s=0
        def bfs(node,depth,sign):
            if not node:
                return 
            if node.val==x or node.val==y:
                an[self.i][0]=depth
                an[self.i][1]=sign
                self.i+=1
                return
            self.s+=1
            sign=self.s 
            bfs(node.left,depth+1,sign)
            bfs(node.right,depth+1,sign)
        bfs(root,0,self.s)  
        return an[0][0]==an[1][0] and an[0][1]!=an[1][1]