class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        le=len(candidates)
        res=[]
        candidates.sort()
        def back(num,index,su):
            if su>target:
                return
            if su==target:
                res.append(num)
                return
            for i in range(index,le):
                if i==index or candidates[i]!=candidates[i-1]:
                    back(num+[candidates[i]],i+1,su+candidates[i])
        back([],0,0)
        return res
        