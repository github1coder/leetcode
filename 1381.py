class CustomStack:

    def __init__(self, maxSize: int):
        self.q=[]
        self.s=0
        self.maxs=maxSize

    def push(self, x: int) -> None:
        if self.s<self.maxs:
            self.q.append(x)
            self.s +=1

    def pop(self) -> int:
        if self.s<=0:
            return -1
        self.s-=1
        return self.q.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i>=self.s:
                break
            self.q[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)