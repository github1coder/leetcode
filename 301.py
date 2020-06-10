class Solution:
    def getremovenum(self,s:str):
        left,right=0,0
        for c in s:
            if c=='(':
                left+=1
            if c==")":
                if left>0:
                    left-=1
                else:
                    right+=1
        return left,right
    def vaild(self,s:str):
        cnt=0
        for c in s:
            if c=='(':
                cnt+=1
            elif c==')':
                cnt-=1
            if cnt<0:
                return False
        return cnt==0
    def removeInvalidParentheses(self, s: str) -> List[str]:
        rmleft,rmright=self.getremovenum(s)
        ans=[]
        def dfs(left:int,right:int,start:int,ss:str):
            if left==right==0 and self.vaild(ss):
                ans.append(ss)
            for i in range(start,len(ss)):
                c=ss[i]
                if i > 0 and ss[i]==ss[i-1]:
                    continue
                if c=='(' and left>0:
                    dfs(left-1,right,i,ss[:i]+ss[i+1:])
                elif c==')' and right>0:
                    dfs(left,right-1,i,ss[:i]+ss[i+1:])
        dfs(rmleft,rmright,0,s)
        return ans