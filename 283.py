class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n>=2:
            i=0
            while i<n-1:
                if nums[i]==0:
                    j=i+1
                    while j<n and nums[j]==0 :
                        j+=1
                    if j>=n:
                        break
                    tem=nums[i]
                    nums[i]=nums[j]
                    nums[j]=tem
                i+=1