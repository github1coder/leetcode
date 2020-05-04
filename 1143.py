class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        le1=len(text1)
        le2=len(text2)
        an=[[0]*(le2+1) for i in range((le1+1))]
        for i in range(1,le1+1):
            for j in range(1,le2+1):
                if text1[i-1]==text2[j-1]:
                    an[i][j]=an[i-1][j-1]+1
                else:
                    an[i][j]=max(an[i-1][j],an[i][j-1])
        return an[le1][le2]
        