# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        def bfs(root,depth):
            if not root: return
            if depth==len(ans):
                ans.insert(0,[])
            ans[-(depth+1)].append(root.val)
            bfs(root.left,depth+1)
            bfs(root.right,depth+1)
        bfs(root,0)
        return ans