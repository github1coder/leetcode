from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        le=len(grid)
        if grid[0][0]==1 or grid[le-1][le-1]==1:
            return -1
        queue=deque()
        queue.append([0,0])
        s=1
        grid[0][0]=1
        while queue:
            s+=1
            le1=len(queue)
            while le1:
                le1-=1
                m,n=queue.popleft()
                if m==le-1 and n==le-1:
                    return s-1 
                if m>0 and n>0 and grid[m-1][n-1]==0:
                    queue.append([m-1,n-1])
                    grid[m-1][n-1]=1
                if m>0 and grid[m-1][n]==0:
                    queue.append([m-1,n])
                    grid[m-1][n]=1 
                if n>0 and grid[m][n-1]==0:
                    queue.append([m,n-1])
                    grid[m][n-1]=1
                if m>0 and n<le-1 and grid[m-1][n+1]==0:
                    queue.append([m-1,n+1])
                    grid[m-1][n+1]=1
                if n<le-1 and grid[m][n+1]==0:
                    queue.append([m,n+1])
                    grid[m][n+1]=1
                if n>0 and m<le-1 and grid[m+1][n-1]==0:
                    queue.append([m+1,n-1])
                    grid[m+1][n-1]=1
                if m<le-1 and grid[m+1][n]==0:
                    queue.append([m+1,n])
                    grid[m+1][n]=1
                if m<le-1 and n<le-1 and grid[m+1][n+1]==0:
                    queue.append([m+1,n+1])
                    grid[m+1][n+1]=1
        return -1      