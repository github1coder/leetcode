# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre=ListNode(0)
        pre.next=head
        p=pre
        for i in range(1,m):
            p=p.next
        km=p.next
        x=km
        y=km.next
        j=m
        while j<n:
            j+=1
            y.next,x=x,y.next
            x,y=y,x
        km.next=y
        p.next=x
        return pre.next
            