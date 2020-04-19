class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q=[]
        self.qmin=[]

    def push(self, x: int) -> None:
        self.q.append(x)
        if not self.qmin or x<=self.qmin[-1]:
            self.qmin.append(x)

    def pop(self) -> None:
        if self.q.pop()==self.qmin[-1]:
            self.qmin.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.qmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()