class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        le=len(candidates)
        res=[]
        candidates.sort()
        def back(num,index,s):
            if s>target:
                return
            if s==target:
                res.append(num)
                return
            for i in range(index,le):
                if i==index or candidates[i]!=candidates[i-1]:
                    back(num+[candidates[i]],i+1,s+candidates[i])
        back([],0,0)
        return res