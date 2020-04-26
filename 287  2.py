class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        le=len(nums)
        left=1
        right=le-1
        while left<right:
            mid=(right+left)//2
            cnt=0
            for num in nums:
                if num<=mid:
                    cnt+=1
            if cnt>mid:
                right=mid
            else:
                left=mid+1
        return left        
