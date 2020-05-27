class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        le=len(nums)
        an=[1]*le
        ma=1
        pre=0
        for i in range(1,le):
            if nums[i]==nums[pre]:
                continue
            if nums[i]==nums[pre]+1:
                an[i]+=an[pre]
            pre=i
            ma=max(ma,an[i])
        return ma
        