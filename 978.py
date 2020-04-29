class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        lenn=len(A)
        if lenn==0 or lenn==1:
            return lenn 
        le=0
        ri=1
        maxn=1
        while ri<lenn:
            if A[ri]>A[le]:
                while ri+1<lenn and A[ri]>A[ri-1] and A[ri]>A[ri+1]:
                    ri+=2
                if ri==lenn:
                    ri-=1
                elif A[ri]<=A[ri-1]:
                    ri-=1
                maxn=max(maxn,ri-le+1)
                le=ri
                ri=le+1
            elif A[ri]<A[le]:
                while ri+1<lenn and A[ri]<A[ri-1] and A[ri]<A[ri+1]:
                    ri+=2
                if ri==lenn:
                    ri-=1
                elif A[ri]>=A[ri-1]:
                    ri-=1
                maxn=max(maxn,ri-le+1)
                le=ri
                ri=le+1
            else:
                le+=1
                ri+=1
        return maxn
        