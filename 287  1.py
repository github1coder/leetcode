class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t1=nums[0]
        t2=nums[0]
        while True:
            t1=nums[t1]
            t2=nums[nums[t2]]
            if t1==t2:
                break
        p1=nums[0]
        while p1!=t1:
            p1=nums[p1]
            t1=nums[t1]
        return t1