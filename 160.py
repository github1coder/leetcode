# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p=headA
        ha={}
        while p:
            ha[p]=1
            p=p.next
        p=headB
        while p:
            if p in ha:
                break
            p=p.next
        return p