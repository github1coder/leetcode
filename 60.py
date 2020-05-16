class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1:
            return "1"
        le=1
        for i in range(2,n):
            le*=i
        num=[]
        an=[i for i in range(1,n+1)]
        def back(index,le,k):
            if index==n-1:
                num.append(str(an[0]))
                return
            t=(k-1)//le
            g=(k-1)%le+1
            num.append(str(an[t]))
            del an[t]
            le=le//(n-1-index)
            back(index+1,le,g)
        back(0,le,k)
        return  ''.join(num)