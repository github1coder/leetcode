class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frep=[0]*26
        le=len(s)
        maxn=0
        wins=0
        maxfrep=0
        if le==0:
            return 0
        for wine in range(le):
            rc=ord(s[wine])-ord('A')
            frep[rc]+=1
            maxfrep=max(maxfrep,frep[rc])
            if (wine-wins+1-maxfrep)>k:
                lf=ord(s[wins])-ord('A')
                wins+=1
                frep[lf]-=1
            maxn=max(maxn,wine-wins+1)
        return maxn
        