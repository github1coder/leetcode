class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        le=len(coins)
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for j in range(le):
                if i-coins[j]>=0 and dp[i-coins[j]]!=-1:
                    if dp[i]==-1:
                        dp[i]=dp[i-coins[j]]+1
                    else:
                        dp[i]=min(dp[i],dp[i-coins[j]]+1)
        return dp[amount]
                    