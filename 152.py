class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        le=len(nums)
        ma=nums[0]
        dp=[[0,0] for i in range(le)]
        dp[0][0]=nums[0]
        dp[0][1]=nums[0]
        for i in range(1,le):
            dp[i][0]=max(nums[i],dp[i-1][0]*nums[i],dp[i-1][1]*nums[i])
            dp[i][1]=min(nums[i],dp[i-1][0]*nums[i],dp[i-1][1]*nums[i])
            ma=max(ma,dp[i][0])
        return ma