class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]

        def op(i,now):
            if now in res:
                return
            res.append(now)
            for j in range(i,n):
                op(j+1,now+[nums[j]])
        op(0,[])
        return res