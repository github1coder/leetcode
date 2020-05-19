class Solution:
    def climbStairs(self, n: int) -> int:
        an=[1]*(n+1)
        for i in range(2,n+1):
            an[i]=an[i-1]+an[i-2]
        return an[n]