class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        le=len(nums)
        if le<3:
            return []
        nums.sort()
        res=[]
        for i in range(le-2):
            if i==0 or nums[i]!=nums[i-1]:
                low=i+1
                high=le-1
                while low<high:
                    if low<high<le-1 and nums[high]==nums[high+1]:
                        high=high-1
                    elif i+1<low<high and nums[low]==nums[low-1]:
                        low=low+1
                    else:
                        if nums[i]+nums[low]+nums[high]>0:
                            high-=1
                        elif nums[i]+nums[low]+nums[high]<0:
                            low+=1
                        else:
                            res.append([nums[i],nums[low],nums[high]])
                            low+=1
                            high-=1
        return res