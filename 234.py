# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.frop=head
        def di(curp=head):
            if curp:
                if not di(curp.next):
                    return False
                if self.frop.val!=curp.val:
                    return False
                self.frop=self.frop.next
            return True
        return di()