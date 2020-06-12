class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f=[float('inf')]*(amount+1)
        f[0]=0
        for c in coins:
            for j in range(c,amount+1):
                f[j]=min(f[j],f[j-c]+1)
        return f[amount] if f[amount]!=float('inf')  else -1