"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p=head
        while p:
            newnode=Node(p.val)
            newnode.next=p.next
            p.next=newnode
            p=newnode.next
        p=head
        while p:
            nexto=p.next.next
            p.next.next=nexto.next if nexto else None
            p.next.random=p.random.next if p.random else None
            p=nexto
        return head.next