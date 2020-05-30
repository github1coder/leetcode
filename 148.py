# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left,right)

    def merge(self,left,right):
        dummy=ListNode(0)
        p=dummy
        l=left
        r=right
        while l and r:
            if l.val<r.val:
                p.next=l
                l=l.next
                p=p.next
            else:
                p.next=r
                r=r.next
                p=p.next
        if l:
            p.next=l
        if r:
            p.next=r
        return dummy.next