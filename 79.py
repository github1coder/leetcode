class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board[0])
        m=len(board)
        le=len(word)
        an=[[0]*n for i in range(m)]
        def back(i,j,index):
            if index==le:
                return True
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= i+dx<m and 0<=j+dy<n and an[i+dx][j+dy]==0 and board[i+dx][j+dy]==word[index]:
                    an[i+dx][j+dy]=1
                    if back(i+dx,j+dy,index+1):
                        return True
                    an[i+dx][j+dy]=0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    an[i][j]=1
                    if back(i,j,1):
                        return True
                    an[i][j]=0
        return False