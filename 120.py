class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        for i in range(1,n):
            for j in range(i+1):
                if j==0:
                    triangle[i][0]+=triangle[i-1][0]
                elif j==i:
                    triangle[i][i]+=triangle[i-1][i-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        mins=triangle[n-1][0]
        for k in range(1,n):
            mins=min(mins,triangle[n-1][k])
        return mins
