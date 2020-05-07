class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        le,masum=len(nums),sum(nums)
        dp=[collections.defaultdict(int) for i in range(le)]
        dp[0][nums[0]]=1
        dp[0][-nums[0]]+=1
        for i in range(1,le):
            for j in range(-masum,masum+1):
                dp[i][j]=dp[i-1].get(j+nums[i],0)+dp[i-1].get(j-nums[i],0)
        return dp[-1][S]