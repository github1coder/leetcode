class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        le=len(nums)
        if le==0:
            return []
        sign=[0]*le
        res=[]
        def back(num,index):
            if index>=le:
                res.append(num)
                return 
            for i in range(le):
                if not (sign[i]==1 or (i>0 and nums[i]==nums[i-1] and sign[i-1]==0)) :
                    sign[i]=1
                    back(num+[nums[i]],index+1)
                    sign[i]=0
        back([],0)
        return res
        