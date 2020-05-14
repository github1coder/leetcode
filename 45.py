class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        le=len(nums)
        i=0
        su=0
        while i<le-1:
            sign=0
            ma=0
            for j in range(1,nums[i]+1):
                if i+j>=le-1:
                    return su+1
                t=i+j+nums[i+j]
                if t>=ma:
                    sign=i+j
                    ma=t
            i=sign
            su+=1
        return su