# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1,s2=[],[]
        sign=0
        res=None
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        while s1 or s2 or sign!=0:
            a=0 if not s1 else s1.pop()
            b=0 if not s2 else s2.pop()
            now=a+b+sign
            sign,now=now//10,now%10
            cur=ListNode(now)
            cur.next=res
            res=cur
        return res