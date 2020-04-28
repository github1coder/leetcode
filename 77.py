class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def back(kn,num,nn):
            if kn==0:
                res.append(num)
                return
            if nn<=n:
                for i in range(nn,n+1):
                    back(kn-1,num+[i],i+1)
        back(k,[],1)
        return res