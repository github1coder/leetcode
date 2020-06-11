class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l=len(prices)
        dp=[[0,0] for _ in range(l+1)]
        dp[0][1]=float('-inf')
        dp[1][1]=-prices[0]
        for i in range(2,l+1):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i-1])
            dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i-1])
        return dp[-1][0]