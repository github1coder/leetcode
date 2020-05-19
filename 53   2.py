class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        le=len(nums)
        an=[0]*le
        ma=-float('inf')
        for i in range(le):
            an[i]=nums[i]
            if i>0 and an[i-1]>0:
                an[i]+=an[i-1]
            ma=max(ma,an[i])
        return ma