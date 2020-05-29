# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not  head:
            return False
        low=head
        fast=head
        while low and fast:
            low=low.next
            fast=fast.next
            if not fast:
                return False
            fast=fast.next
            if low==fast:
                return True
        return False