class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma=0
        le=len(s)
        l=r=0
        dic={}
        while r<le:
            if s[r] not in dic:
                dic[s[r]]=r
                r+=1
            else:
                ma=max(ma,r-l)
                del dic[s[l]]
                l+=1
        ma=max(ma,r-l)
        return ma 
        