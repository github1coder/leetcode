class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def divide(lo,hi):
            if lo==hi:
                return nums[lo]
            mid=(hi+lo)//2
            left=divide(lo,mid)
            right=divide(mid+1,hi)
            if left==right:
                return left
            leftc=sum(1 for i in range(lo,hi+1) if nums[i]==left)
            rightc=sum(1 for i in range(lo,hi+1) if nums[i]==right)
            if leftc>rightc:
                return left
            else:
                return right
        return divide(0,len(nums)-1)