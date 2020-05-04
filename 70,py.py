class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        an=[0]*(n+1)
        an[0]=1
        an[1]=1
        for i in range(2,n+1):
            an[i]=an[i-1]+an[i-2]
        return an[n]