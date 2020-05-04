class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=max(nums[i-1],0)
            ma=max(nums[i],ma)
        return ma