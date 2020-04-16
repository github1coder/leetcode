# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<=l2.val:
            i=l1
            j=l2
        else:
            i=l2
            j=l1
        while i!=None or j!=None:
            if i==None:
                pi.next=j
                break
            elif j==None:
                break
            else:
                if i.val<=j.val:
                    pi=i
                    i=i.next
                else:
                    pi.next=j
                    j=j.next
                    pi=pi.next
                    pi.next=i
        if l1.val<=l2.val:
            return l1

        else :
            return l2

