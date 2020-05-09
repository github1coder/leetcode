# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pr=ListNode
        pre=ListNode
        pr.next=pre.next=p=q=head
        for i in range(n):
            q=q.next
        while q:
            pre,p,q=pre.next,p.next,q.next
        pre.next=p.next
        return pr.next