class Solution:
    def dfs(self,board,x,y):
        board[x][y]='k'
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            if 0<=x+dx<self.lm and 0<=y+dy<self.ln and board[x+dx][y+dy]=='O':
                self.dfs(board,x+dx,y+dy)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.lm=len(board)
        if self.lm==0:
            return 
        self.ln=len(board[0])
        for j in range(self.ln):
            if board[0][j]=='O':
                self.dfs(board,0,j)
            if board[self.lm-1][j]=='O':
                self.dfs(board,self.lm-1,j)
        for j in range(self.lm):
            if board[j][0]=='O':
                self.dfs(board,j,0)
            if board[j][self.ln-1]=='O':
                self.dfs(board,j,self.ln-1)        
        for i in range(self.lm):
            for j in range(self.ln):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='k':
                    board[i][j]='O'
        return