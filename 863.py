# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.num=[]
        self.node=None
        def dfs(node,nums):
            if not node: return 
            if node==target:
                self.num=[item for item in nums]
                self.node=node
                return 
            dfs(node.left,nums+[node])
            dfs(node.right,nums+[node])
        dfs(root,[])
        le=len(self.num)
        visited={}
        key=[]
        def dis(node,depth,sign):
            if not node : return
            visited[node]=1 
            if depth==K:
                key.append(node.val)
                return
            if node.left and node.left not in visited:
                dis(node.left,depth+1,0)
            if node.right and node.right not in visited:
                dis(node.right,depth+1,0)
            if sign==1 and depth+1<=le:
                dis(self.num[-(depth+1)],depth+1,1)
        dis(self.node,0,1)
        return key