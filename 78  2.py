class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        le=len(nums)
        res=[]
        def back(num,index):
            if index==le:
                res.append(num)
                return 
            back(num+[],index+1)
            back(num+[nums[index]],index+1)
        back([],0)
        return res