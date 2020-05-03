class Solution:
    def find(self,index,pre):
        if pre[index]==index:
            return index
        return self.find(pre[index],pre)
    def findCircleNum(self, M: List[List[int]]) -> int:
        n=len(M)
        pre=list(range(n))
        num=n
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    idi=self.find(i,pre)
                    idj=self.find(j,pre)
                    if idi !=idj:
                        pre[idi]=idj
                        num-=1
        return num