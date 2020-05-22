class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea=0
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    continue
                width=dp[i][j]=dp[i][j-1]+1 if j else 1
                for k in range(i,-1,-1):
                    width=min(width,dp[k][j])
                    maxarea=max(maxarea,width*(i-k+1))
        return maxarea