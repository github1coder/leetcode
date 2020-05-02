"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited={}
        queue=deque([node])
        visited[node]=Node(node.val,[])
        while queue:
            n=queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei]=Node(nei.val,[])
                    queue.append(nei)
                visited[n].neighbors.append(visited[nei])
        return visited[node]