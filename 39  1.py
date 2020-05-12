class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        le=len(candidates)
        res=[]
        def back(num,index,su):
            if su==target:
                res.append(num)
                return
            if su>target:
                return 
            if index<le:
                for i in range(index,le):
                    if i ==index or candidates[i]!=candidates[i-1]:
                        back(num+[candidates[i]],i,su+candidates[i])
        back([],0,0)
        return res
        