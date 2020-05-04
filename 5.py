class Solution:
    def longestPalindrome(self, s: str) -> str:
        le=len(s)
        if le==0:
            return ""
        a=0
        b=0
        dp=[[1]*le for i in range(le)]
        for l in range(1,le):
            for i in range(le-l):
                if dp[i+1][i+l-1]!=1 or s[i]!=s[i+l]:
                    dp[i][i+l]=0
                elif l>b-a:
                    a,b=i,i+l
        return s[a:b+1]