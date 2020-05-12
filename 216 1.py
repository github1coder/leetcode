class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def back(num,index,su,kn):
            if su==n and kn==0:
                res.append(num)
                return 
            if kn==0 or su>n:
                return
            for i in range(index,10):
                back(num+[i],i+1,su+i,kn-1)
        back([],1,0,k)
        return res