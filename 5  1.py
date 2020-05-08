class Solution:
    def longestPalindrome(self, s: str) -> str:
        le=len(s)
        if le==0:
            return ""
        mi,ma=0,0
        res=[[i,i+1] for i in range(le)]
        for i in range(1,le):
            for j in res[i-1]:
                if j>0 and s[i]==s[j-1]:
                    res[i].append(j-1)
                    if i-j+2>ma-mi+1:
                        ma,mi=i,j-1
        return s[mi:ma+1]
