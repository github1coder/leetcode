class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1 for _ in range(n)]
        i2=0
        i3=0
        i5=0
        for i in range(1,n):
            minval=min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            dp[i]=minval
            if dp[i2]*2==minval:
                i2+=1
            if dp[i3]*3==minval:
                i3+=1
            if dp[i5]*5==minval:
                i5+=1
        return dp[-1]