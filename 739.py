class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        le=len(T)
        an=[0]*le
        zhan=[]
        for i in range(le):
            if not zhan or T[zhan[-1]]>=T[i]:
                zhan.append(i)
            else:
                while zhan and T[zhan[-1]]<T[i]:

                    s=zhan.pop()
                    
                    an[s]=i-s
                zhan.append(i)
        return an