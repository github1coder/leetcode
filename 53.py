class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide(lo,hi):
            if lo==hi:
                return nums[lo]
            mid=(lo+hi)//2
            left=divide(lo,mid)
            right=divide(mid+1,hi)
            su=nums[mid]+nums[mid+1]
            i=mid-1
            t=su 
            while i>=lo:
                t=t+nums[i]
                su=max(su,t)
                i-=1
            t=su
            i=mid+2
            while i<=hi:
                t=t+nums[i]
                su=max(su,t)
                i+=1
            return max(left,right,su)
        return divide(0,len(nums)-1)