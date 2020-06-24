class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        s=sorted(nums,reverse=True)
        res=[]
        dic={}
        start=1
        le=len(nums)
        for i,val in enumerate(s):
            if start==1:
                dic[val]="Gold Medal"
            elif start==2:
                dic[val]="Silver Medal"
            elif start==3:
                dic[val]="Bronze Medal"
            else:
                dic[val]=str(start)
            start+=1
        for i in range(len(nums)):
            res.append(dic.get(nums[i]))
        return res