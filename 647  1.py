class Solution:
    def countSubstrings(self, s: str) -> int:
        le=len(s)
        n=le
        an=[[i,i+1] for i in range(le)]
        for i in range(1,le):
            for j in an[i-1]:
                if j-1>=0:
                    if s[i]==s[j-1]:
                        n+=1
                        an[i].append(j-1)
        return n
