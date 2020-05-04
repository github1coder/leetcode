class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[float('inf') for i in range(n)]  for j in range(n)]
        ma=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i,n):
                ma[i][j]=max(arr[i:j+1])
        for i in range(n):
            dp[i][i]=0
        for i in range(1,n):
            for s in range(n-i):
                for k in range(s,s+i):
                    dp[s][s+i]=min(dp[s][s+i],dp[s][k]+dp[k+1][s+i]+ma[s][k]*ma[k+1][s+i])
        return dp[0][n-1]