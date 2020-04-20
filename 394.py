class Solution:
    def decodeString(self, s: str) -> str:
        stack,res,mu=[],"",0
        for c in s:
            if c=='[':
                stack.append([mu,res])
                res,mu="",0
            elif c==']':
                cmu,lres=stack.pop()
                res=lres+cmu*res
            elif '0'<=c<='9':
                mu=mu*10+int(c)
            else:
                res+=c
        return res
