class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        dic={}
        def back(num,index,k,s):
            if k==1:
                t=n-s 
                if index <= t <= 9:
                    res.append(num+[t])
                return 
            for i in range(index,10):
                back(num+[i],i+1,k-1,s+i)                
        back([],1,k,0)
        return res