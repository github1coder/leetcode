class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j=len(nums)-1
        i=0
        while i<=j:
            mid =(i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return i