class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        le=len(nums)
        num=[]
        for i in range(le):
            j=(i+1)%le
            while j!=i:
                if nums[j]>nums[i]:
                    num.append(nums[j])
                    break
                j=(j+1)%le
            if j==i:
                num.append(-1)
        return num