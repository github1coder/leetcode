class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        su=0
        m=len(grid)
        n=len(grid[0])
        an=[[0]*n for _ in range(m)]
        def dfs(i,j):
            grid[i][j]='0'
            an[i][j]=1
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y=i+dx,j+dy
                if 0<=x<m and 0<=y<n and grid[x][y]=='1' and an[x][y]==0:
                    dfs(x,y)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    su+=1
                    dfs(i,j)
        return su
