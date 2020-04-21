class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        nums=[]
        for [a,b] in points:
            c=a*a+b*b
            if not nums:
                nums.append([[a,b],c])
                continue
            low=0
            le=len(nums)
            if le>K:
                le=K 
            high=le-1
            while low<high:
                mid=(low+high)//2
                if nums[mid][1]>c:
                    high=mid-1
                elif nums[mid][1]<c:
                    low=mid+1
                else:
                    nums.insert(mid,[[a,b],c])
                    break
            if low>=high:
                if nums[low][1]>c:
                    nums.insert(low,[[a,b],c])
                else:
                    nums.insert(low+1,[[a,b],c])
        num=[]
        for i in range(K):
            num.append(nums[i][0])
        return num