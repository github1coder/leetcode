class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        le=len(nums)
        if le==1:
            return nums[0]
        if le==2:
            return max(nums[0],nums[1])
        nums[1]=max(nums[1],nums[0])
        for i in range(2,le):
            nums[i]=max(nums[i]+nums[i-2],nums[i-1])
        return max(nums[le-1],nums[le-2])