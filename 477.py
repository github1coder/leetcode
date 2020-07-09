class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        for i in range(32):
            cnt=0
            for j in range(n):
                cnt+=(nums[j]>>i)&1
            res+=(n-cnt)*cnt
        return res