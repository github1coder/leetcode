class Solution:
    def decodeString(self, s: str) -> str:
        stack,res,multi=[],"",0
        for c in s:
            if c=='[':
                stack.append([multi,res])
                res,multi="",0
            elif c==']':
                curmulti,lastres=stack.pop()
                res=lastres+curmulti*res
            elif '0'<=c<='9':
                multi=multi*10+int(c)
            else:
                res+=c
        return res