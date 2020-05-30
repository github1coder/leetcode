class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.pre=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.ha=dict()
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.pre=self.head
        self.size=0

    def get(self, key: int) -> int:
        if key not in self.ha:
            return -1
        node=self.ha[key]
        self.movetohead(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.ha:
            node=Node(key,value)
            self.ha[key]=node
            self.addtohead(node)
            self.size+=1
            if self.size>self.capacity:
                removed=self.removetail()
                self.ha.pop(removed.key)
                self.size-=1
        else:
            node=self.ha[key]
            node.value=value
            self.movetohead(node)

    def addtohead(self,node):
        node.pre=self.head
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node

    def removenode(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre

    def movetohead(self,node):
        self.removenode(node)
        self.addtohead(node)

    def removetail(self):
        node=self.tail.pre
        self.removenode(node)
        return node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)