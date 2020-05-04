class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0]=='0':
            return 0
        le=len(s)
        dp=[0]*(le+1)
        dp[0]=1
        dp[1]=1
        wro=0
        for i in range(2,le+1):
            t=int(s[i-2])*10+int(s[i-1])
            if t==10 or t==20:
                dp[i]=dp[i-2]
            elif t%10==0:
                wro=1
                break
            elif 10<t<=26:
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        if wro==1:
            return 0
        return dp[le]