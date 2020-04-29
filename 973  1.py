class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        nums=[i*i+j*j  for i,j in points]
        def divide(lo,hi):
            if hi-lo+1<=K:
                return [i for i in range(lo,hi+1)]
            mid=(lo+hi)//2
            left=divide(lo,mid)
            right=divide(mid+1,hi)
            nu=left+right
            nu.sort(key=lambda j:nums[j])
            return nu[:K]
        res=divide(0,len(points)-1)
        return [points[item] for item in res]