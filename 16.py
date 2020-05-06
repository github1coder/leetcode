class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        le=len(nums)
        mi=float('inf')
        nums.sort()
        for i in range(le-2):
            low=i+1
            high=le-1
            while low<high:
                t=nums[i]+nums[low]+nums[high]
                if abs(t-target) < abs(mi-target):
                    mi=t
                if t-target>0:
                    high-=1
                elif t-target<0:
                    low+=1
                else:
                    break
        return mi
                    