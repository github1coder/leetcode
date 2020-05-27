class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        le=len(prices)
        ma=0
        mi=prices[0]
        for i in range(1,le):
            if prices[i]-mi>ma:
                ma=prices[i]-mi
            if prices[i]<mi:
                mi=prices[i]

        return ma
