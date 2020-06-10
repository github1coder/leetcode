class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        le=len(nums)
        dp=[1]*le
        ma=1
        for i in range(1,le):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                    ma=max(ma,dp[i])
        return ma