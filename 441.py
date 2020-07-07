class Solution:
    def arrangeCoins(self, n: int) -> int:
        s=0
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(1,n+1):
            s+=i
            if s>n:
                return i-1
            if s==n:
                return i