class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs=1
        le=len(s)
        if le==0:
            return 0
        for i in range(le):
            ma=0
            dic={}
            for j in range(i,le):
                if s[j] not in dic:
                    dic[s[j]]=1
                    ma+=1
                else:
                    break
            maxs=max(maxs,ma)
        return maxs