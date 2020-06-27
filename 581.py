class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        ma=nums[0]
        right=0
        for i in range(n):
            if nums[i]>ma:
                ma=nums[i]
            elif nums[i]<ma:
                right=i
        mi=nums[-1]
        left=n-1
        for i in range(n-1,-1,-1):
            if nums[i]<mi:
                mi=nums[i]
            elif nums[i]>mi:
                left=i
        if left>=right:
            return 0
        return right-left+1
        