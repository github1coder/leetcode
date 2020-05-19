class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        an=[[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                an[i][j]=an[i][j-1]+an[i-1][j]
        return an[m-1][n-1]