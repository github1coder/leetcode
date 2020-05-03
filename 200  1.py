class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.s=0
        lm=len(grid)
        if lm==0:
            return 0
        ln=len(grid[0])
        def dfs(m,n):
            grid[m][n]='0'
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0<=m+dx<lm and 0<=n+dy<ln and grid[m+dx][n+dy]=='1':
                    dfs(m+dx,n+dy)
        for i in range(lm):
            for j in range(ln):
                if grid[i][j]=='1':
                    self.s+=1
                    dfs(i,j)
        return self.s