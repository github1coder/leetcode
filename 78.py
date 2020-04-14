class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)

        def op(i,now):
            res.append(now)
            for j in range(i,n):
                op(j+1,now+[nums[j]])
        
        op(0,[])
        return res