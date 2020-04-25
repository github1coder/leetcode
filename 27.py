class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        le=len(nums)
        j=le-1
        while i<=j:
            if nums[i]==val:
                nums[i]=nums[j]
                j-=1
                le-=1
            else:
                i+=1
        return le