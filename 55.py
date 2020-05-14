class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        le=len(nums)
        i=le-1
        j=le-2
        while j>=0:
            if j>=0 and j+nums[j]>=i:
                i=j
            j-=1
        return i==0