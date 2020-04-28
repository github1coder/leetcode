class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        le=len(nums)
        if le==0:
            return []
        res=[]
        def back(path,index):
            if index>le:
                return 
            res.append(path)
            for i in range(index,le):
                back(path+[nums[i]],i+1)
        back([],0)
        return res
        