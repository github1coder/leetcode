# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not  head:
            return None
        low=head
        fast=head
        while low and fast:
            low=low.next
            fast=fast.next
            if not fast:
                return None
            fast=fast.next
            if low==fast:
                low=head
                while low!=fast:
                    fast=fast.next
                    low=low.next
                return low
        return None