# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p=head
        while p!=None:
            if p.val==val:
                if p == head:
                    head=head.next
                    p=head
                else :
                    q.next=p.next
                    p=p.next
            else :
                q=p
                p=p.next
        return head