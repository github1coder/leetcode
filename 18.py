class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        le=len(nums)
        if le<4:
            return []
        nums.sort()
        res=[]
        for a in range(le-3):
            if a==0 or nums[a]!=nums[a-1]:
                for b in range(a+1,le-2):
                    if b==a+1 or nums[b]!=nums[b-1]:
                        c=b+1
                        d=le-1
                        while c<d:
                            if d>c>b+1 and nums[c]==nums[c-1]:
                                c+=1
                            elif c<d<le-1 and nums[d]==nums[d+1]:
                                d-=1
                            else:
                                t=nums[a]+nums[b]+nums[c]+nums[d]-target
                                if t<0:
                                    c+=1
                                elif t>0:
                                    d-=1
                                else:
                                    res.append([nums[a],nums[b],nums[c],nums[d]])
                                    c+=1
                                    d-=1
        return res