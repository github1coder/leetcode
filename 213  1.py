class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        an=[0]*(n+1)
        bn=[0]*(n+1)
        an[1]=nums[0]
        an[2]=nums[0]
        for i in range(3,n):
            an[i]=max(nums[i-1]+an[i-2],an[i-1])
        for i in range(2,n+1):
            bn[i]=max(nums[i-1]+bn[i-2],bn[i-1])
        return max(an[n-1],bn[n])