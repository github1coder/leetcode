class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=collections.Counter(s1)
        c2=collections.Counter()
        l1=len(s1)
        l2=len(s2)
        p=q=0
        while q<l2:
            c2[s2[q]]+=1
            if c1==c2:
                return True
            q+=1
            if q-p+1>l1:
                c2[s2[p]]-=1
                if c2[s2[p]]==0:
                    del c2[s2[p]]
                p+=1
        return False
        