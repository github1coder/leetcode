class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        le=len(candidates)
        def back(num,index,s):
            if s>target:
                return
            if s==target:
                res.append(num)
                return 
            for i in range(index,le):
                back(num+[candidates[i]],i,s+candidates[i])
        back([],0,0)
        return res