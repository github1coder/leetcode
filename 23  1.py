# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        dummy=ListNode(None)
        node=dummy
        ptrs=[head for head in lists]
        ptrs=list(filter(lambda x: x!=None,ptrs))
        while ptrs:
            tmp=[node.val for node in ptrs]
            cur=min(tmp)
            minidx=tmp.index(cur)
            node.next=ptrs[minidx]
            ptrs[minidx]=ptrs[minidx].next
            if not ptrs[minidx]:
                del ptrs[minidx]
            node=node.next
        return dummy.next