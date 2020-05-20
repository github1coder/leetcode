class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le=len(nums)
        i=0
        j=le-1
        n=0
        while n<le:
            if nums[n]==0 and n>i:
                nums[n],nums[i]=nums[i],nums[n]
                i+=1
            elif nums[n]==2 and n<j:
                nums[n],nums[j]=nums[j],nums[n]
                j-=1
            else:
                n+=1