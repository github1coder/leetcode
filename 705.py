class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}

    def add(self, key: int) -> None:
        self.dic[key]=key

    def remove(self, key: int) -> None:
        if key in self.dic:
            del self.dic[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.dic:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)