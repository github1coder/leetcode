class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        le=len(nums)
        res=[]
        check=[0]*le
        def back(num,index):
            if index==le:
                res.append(num)
                return
            if not (index>0 and nums[index]==nums[index-1] and check[index-1]==0):
                check[index]=1
                back(num+[nums[index]],index+1)
                check[index]=0
            back(num,index+1)
        back([],0)
        return res