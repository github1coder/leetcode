class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        le=len(nums)
        an=[0]*(le+2)
        an[0]=1
        for num in nums:
            if 0<num<le+2:
                an[num]=1
        for i in range(le+2):
            if an[i]==0:
                return i