class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        le=len(stones)
        while le>1:
            a=stones.pop()
            b=stones.pop()
            a=a-b
            le-=2
            if a!=0 :
                if le==0:
                    stones.append(a)
                    le+=1
                    continue
                low=0
                high=le-1
                while low<high:
                    mid=(low+high)//2
                    if stones[mid]<a:
                        low=mid+1
                    else:
                        high=mid-1
                if low==0:
                    if stones[0]>a:
                        stones.insert(0,a)
                    else:
                        stones.insert(1,a)
                elif high==le-1:
                    if stones[le-1]>a:
                        stones.insert(le-1,a)
                    else:
                        stones.append(a)
                else:
                    if stones[low]>a:
                        stones.insert(low,a)
                    else:
                        stones.insert(low+1,a)
                le+=1
        if not stones:
            return 0
        return stones[0]
