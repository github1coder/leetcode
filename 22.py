class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def back(s,left,right):
            if left==0 and right==0:
                res.append(s)
                return 
            if left>0:
                back(s+'(',left-1,right)
            if right>left:
                back(s+')',left,right-1)
        back("",n,n)
        return res