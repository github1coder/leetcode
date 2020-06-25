class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        le=len(nums)
        s=0
        for i in nums:
            s=s+i
        if s%2!=0:
            return False
        s=s//2
        dp=[[False]*(s+1) for _ in range(le)]
        for i in range(le):
            dp[i][0]=True
        for j in range(1,s+1):
            if nums[0]==j:
                dp[0][j]=True
        for i in range(1,le):
            for j in range(1,s+1):
                if dp[i-1][j]==True:
                    dp[i][j]=True
                elif j-nums[i]>=0 and dp[i-1][j-nums[i]]==True:
                    dp[i][j]=True
        return dp[le-1][s]
