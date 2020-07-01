class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        le=len(nums)
        s=1
        sign=0
        for i in range(le):
            if (nums[i]!=0):
                s*=nums[i]
            else:
                sign+=1
        output=[0]*le
        for i in range(le):
            if nums[i]!=0 and sign==0:
                output[i]=s//nums[i]
            elif nums[i]==0 and sign-1<=0:
                output[i]=s
        return output