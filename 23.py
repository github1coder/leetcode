# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root=ListNode()
        p=root
        le=len(lists)
        while 1:
            mi=999999999999
            sign=-1
            i=0
            while i<le:
                if lists[i]!=None:
                    if lists[i].val<mi:
                        mi=lists[i].val
                        sign=i
                    i+=1
                else:
                    del lists[i]
                    le-=1
            if le==1:
                p.next=lists[0]
                break
            if sign==-1:
                break
            p.next=lists[sign]
            p=p.next
            lists[sign]=lists[sign].next
        return root.next