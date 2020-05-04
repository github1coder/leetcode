class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        le=len(prices)
        if le==0:
            return 0
        mi=prices[0]
        ma=0
        for i in range(1,le):
            ma=max(ma,prices[i]-mi)
            mi=min(mi,prices[i])
        return ma