class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        le=len(nums)
        low,high=0,le-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                break
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if low>high:
            return [-1,-1]
        ri=mid
        lef=mid
        while low<=ri:
            mid=(low+ri)//2
            if nums[mid]<target:
                low=mid+1
            else:
                ri=mid-1
        while lef<=high:
            mid=(lef+high)//2
            if nums[mid]>target:
                high=mid-1
            else:
                lef=mid+1
        return [low,high]