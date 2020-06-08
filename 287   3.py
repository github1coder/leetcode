class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        an=[0]*(n+1)
        for num in nums:
            if an[num]!=0:
                return num
            an[num]=1