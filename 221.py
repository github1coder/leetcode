class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ma=0
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    ma=max(ma,dp[i][j])
        return ma*ma