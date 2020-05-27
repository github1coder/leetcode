class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        le=len(nums)
        a=nums[0]
        for i in range(1,le):
            a^=nums[i]
        return a