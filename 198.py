class Solution:
    def rob(self, nums: List[int]) -> int:
        le=len(nums)
        if le==0:
            return 0
        an=[[0]*2 for i in range(le)]
        an[0][0]=0
        an[0][1]=nums[0]
        for i in range(1,le):
            an[i][0]=max(an[i-1][0],an[i-1][1])
            an[i][1]=an[i-1][0]+nums[i]
        return max(an[le-1][0],an[le-1][1])