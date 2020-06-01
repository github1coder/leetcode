class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.zhan=[]
        self.fu=[]

    def push(self, x: int) -> None:
        if not self.zhan:
            self.zhan.append(x)
            self.fu.append(x)
        else:
            self.zhan.append(x)
            self.fu.append(min(x,self.fu[-1]))
    def pop(self) -> None:
        self.zhan.pop()
        self.fu.pop()
    def top(self) -> int:
        return self.zhan[-1]


    def getMin(self) -> int:
        return self.fu[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()