class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        le=len(nums)
        nums.sort()
        res=[]
        an=[0]*le
        def back(num,su):
            if su==le:
                res.append(num)
                return 
            for i in range(le):
                if (an[i]==0) and not (i>0 and nums[i]==nums[i-1] and an[i-1]==0):
                    an[i]=1
                    back(num+[nums[i]],su+1)
                    an[i]=0
        back([],0)
        return res