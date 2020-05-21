from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dic=Counter(t)
        requierd=len(dic)
        l,r=0,0
        formed=0
        win=defaultdict(int)
        ans=float("inf"),None,None
        while r<len(s):
            cha=s[r]
            win[cha]+=1
            if cha in dic and win[cha]==dic[cha]:
                formed+=1
            while l<=r and formed==requierd:
                cha=s[l]
                if r-l+1<ans[0]:
                    ans=(r-l+1,l,r)
                win[cha]-=1
                if cha in dic and win[cha]<dic[cha]:
                    formed-=1
                l+=1
            r+=1
        return "" if ans[0]==float("inf")  else s[ans[1]:ans[2]+1]