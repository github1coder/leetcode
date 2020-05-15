class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le=len(nums)
        if le==1:
            return nums
        i=le-2
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        if i<0:
            return nums.sort()
        mi=float('inf')
        sign=0
        for j in range(le-1,i,-1):
            if nums[j]>nums[i] and nums[j]<mi:
                sign=j
                mi=nums[j]
        nums[i],nums[sign]=nums[sign],nums[i]
        nums[i+1:]=sorted(nums[i+1:])
        return nums