class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<2:
            return 0
        max1=0
        now=prices[0]
        sign=0
        for i in range(1,n):
            if prices[i]-now>max1:
                max1=prices[i]-now
            if prices[i]<now:
                now=prices[i]
        return max1
            