# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root=ListNode()
        m=root
        p,q=l1,l2
        while p and q:
            m.next=ListNode()
            m=m.next
            if p.val<q.val:
                m.val=p.val
                p=p.next
            else:
                m.val=q.val
                q=q.next
        if p:
            m.next=p
        else:
            m.next=q
        return root.next