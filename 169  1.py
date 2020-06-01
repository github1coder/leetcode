class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        le=len(nums)
        def half(low,high):
            if low==high:
                return nums[low]
            mid=(low+high)//2
            l=half(low,mid)
            ri=half(mid+1,high)
            if l==ri:
                return l
            lenn=rin=0
            for i in range(low,high+1):
                if nums[i]==l:
                    lenn+=1
                elif nums[i]==ri:
                    rin+=1
            if lenn>rin:
                return l
            return ri
        return half(0,le-1)
        