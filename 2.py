# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sign=0
        p=ListNode(1)
        p.next=l1
        i=l1
        j=l2
        while i!=None and j!=None:
            i.val=i.val+j.val+sign
            i.val,sign=int(i.val % 10),int(i.val/10)
            p=i
            i=i.next
            j=j.next
        if i==None:
            p.next=j
            i=p.next
        while sign==1:
            if i==None:
                p.next=ListNode(1)
                p.next.next=None
                sign=0
            else:
                i.val=i.val+sign
                i.val,sign=int(i.val % 10),int(i.val/10)
                p=i 
                i=i.next
        return l1