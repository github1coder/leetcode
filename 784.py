class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res=[]
        def back(s,i):
            res.append(s)
            for k in range(i,len(s)):
                if 'a'<=s[k]<='z':
                    back(s[:k]+s[k].upper()+s[k+1:],k+1)
                elif 'A'<=s[k]<='Z':
                    back(s[:k]+s[k].lower()+s[k+1:],k+1)
            
        back(S,0)
        return res