class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount=[0]*26
        scount=[0]*26
        res=[]
        for a in p:
            pcount[ord(a)-97]+=1
        left=0
        for right in range(len(s)):
            if right<len(p)-1:
                scount[ord(s[right])-97]+=1
                continue
            scount[ord(s[right])-97]+=1
            if scount==pcount:
                res.append(left)
            scount[ord(s[left])-97]-=1
            left+=1
        return res
