# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        pre=ListNode(0)
        pre.next=head
        p=pre
        he=head
        k=head.next
        while k!=None and he!=None:
            k.next,he=he,k.next
            k.next.next=he
            p.next=k
            p=k.next
            if he!=None:
                k=he.next
            else:
                k=he
                
        return pre.next