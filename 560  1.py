class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={}
        co=0
        le=len(nums)
        for i in range(le):
            if i>0:
                nums[i]+=nums[i-1]
            if nums[i]==k:
                co+=1
        for num in nums:
            if num-k in dic:
                co+=dic[num-k]
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1  
        return co