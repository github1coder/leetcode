class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s=0
        lm=len(grid)
        if lm ==0:
            return 0
        ln=len(grid[0])
        def bfs(m,n):
            grid[m][n]="0"
            if m>0 and grid[m-1][n]=="1":
                bfs(m-1,n)
            if n>0 and grid[m][n-1]=="1":
                bfs(m,n-1)
            if m<lm-1 and grid[m+1][n]=="1":
                bfs(m+1,n)
            if n<ln-1 and grid[m][n+1]=="1":
                bfs(m,n+1)
        for m in range(lm):
            for n in range(ln):
                if grid[m][n]=="1":
                    s+=1
                    bfs(m,n)
        return s