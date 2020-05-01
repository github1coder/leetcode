"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans=0
        def bfs(node,depth):
            if not node:
                return 0
            s=0
            for t in node.children:
                s+=bfs(t,depth+1)
            if s==0:
                self.ans=max(self.ans,depth)
            return 1
        bfs(root,1)
        return self.ans