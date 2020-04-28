class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num<0:
            return []
        res=[]
        h=[1,2,4,8]
        m=[1,2,4,8,16,32]
        def back(num,index,st):
            if num==0:
                ho=0
                mi=0
                for i in range(4):
                    ho+=st[i]*h[i]
                for i in range(4,10):
                    mi+=st[i]*m[i-4]
                if ho<12 and mi<60:
                    res.append('%d:%02d' %(ho,mi))
                    return
            for i in range(index,10):
                st[i]=1
                back(num-1,i+1,st)
                st[i]=0
        back(num,0,[0]*10)
        return res