class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        for j in range(n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1