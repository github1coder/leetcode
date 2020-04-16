# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic={}
        
        k=head
        while k!=None:
            if k in dic:
                return k
            dic[k]=1
            k=k.next
        return None