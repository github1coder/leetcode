class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        le=len(nums)
        zero=0
        fei=0
        while fei<le and zero<le:
            while zero<le and nums[zero]!=0 :
                zero+=1
            fei=zero+1
            while  fei<le and nums[fei]==0:
                fei+=1
            if zero<le and fei<le:
                nums[zero],nums[fei]=nums[fei],nums[zero]
            zero+=1