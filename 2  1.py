# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r=root=ListNode((l1.val+l2.val)%10)
        sign=(l1.val+l2.val)//10
        p=l1.next
        q=l2.next
        while p and q:
            r.next=ListNode()
            r=r.next
            s=p.val+q.val+sign
            r.val=s%10
            sign=s//10
            p,q=p.next,q.next
        while p:
            r.next=ListNode()
            r=r.next
            s=p.val+sign
            r.val=s%10
            sign=s//10
            p=p.next
        while q:
            r.next=ListNode()
            r=r.next
            s=q.val+sign
            r.val=s%10
            sign=s//10
            q=q.next
        if sign!=0:
            r.next=ListNode(1)
            r=r.next
            r.next=None
        else:
            r.next=None
        return root