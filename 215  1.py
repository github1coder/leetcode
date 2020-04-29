class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def divide(lo,hi):
            if hi-lo+1<=k:
                nu=[nums[item] for item in range(lo,hi+1)]
                nu.sort(reverse=True)
                return nu
            mid=(lo+hi)//2
            left=divide(lo,mid)
            right=divide(mid+1,hi)
            nu=left+right
            nu.sort(reverse=True)
            return nu[:k]
        sn=divide(0,len(nums)-1)
        return sn[k-1]