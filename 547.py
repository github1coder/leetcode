class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        lm=len(M)
        ln=len(M[0])
        def dfs(m):
            s=0
            for i in range(ln):
                if M[m][i]==1:
                    s=1
                    M[m][i]=0
                    if m!=i:
                        dfs(i)
            return s
        su=0
        for mm in range(lm):
            su+=dfs(mm)
        return su
