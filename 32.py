class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ma=0
        le=len(s)
        if le==0:
            return 0
        an=[0]*le
        for i in range(le):
            if s[i]==')':
                if i-1>=0 and s[i-1]=='(':
                    if i-2<0:
                        an[i]=2
                    else:
                        an[i]=an[i-2]+2
                    ma=max(ma,an[i])
                elif i-1>0 and s[i-1]==')':
                    if i-an[i-1]-1>=0 and s[i-an[i-1]-1]=='(':
                        if i-an[i-1]-1>=0:
                            an[i]=an[i-1]+2+an[i-an[i-1]-2]
                        else:
                            an[i]=an[i-1]+2
                        ma=max(ma,an[i])
        return ma