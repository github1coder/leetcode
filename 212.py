class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            t=trie
            for w in word:
                t=t.setdefault(w,{})
            t["end"]=1
        res=[]
        row=len(board)
        col=len(board[0])
        def dfs(i,j,trie,s):
            c=board[i][j]
            if c not in trie:return
            trie=trie[c]
            if "end" in trie and trie["end"]==1:
                res.append(s+c)
                trie["end"]=0
            board[i][j]="#"
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                x=i+dx
                y=j+dy
                if 0<=x<row and 0<=y<col and board[x][y]!="#":
                    dfs(x,y,trie,s+c)
            board[i][j]=c
        for i in range(row):
            for j in range(col):
                dfs(i,j,trie,"")
        return res