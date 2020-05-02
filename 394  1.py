class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s,i):
            res=""
            mu=0
            while i<len(s):
                if '0'<=s[i]<='9':
                    mu=mu*10+int(s[i])
                elif s[i]=='[':
                    i,tmp=dfs(s,i+1)
                    res+=mu*tmp
                    mu=0
                elif s[i]==']':
                    return i,res
                else:
                    res+=s[i]
                i+=1
            return res
        return dfs(s,0)
        