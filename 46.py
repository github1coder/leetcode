class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        le=len(nums)
        if le==0:
            return []
        res=[]
        def back(path,depth,dic):
            if depth==le:
                res.append([item for item in path])
                return 
            for i in nums:
                if i not in dic:
                    dic[i]=1
                    path.append(i)
                    back(path,depth+1,dic)
                    path.pop()
                    del dic[i]
        back([],0,{})
        return res