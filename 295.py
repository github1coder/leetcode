class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n=0
        self.data=[]

    def addNum(self, num: int) -> None:
        if self.n==0:
            self.data.append(num)
            self.n+=1
            return
        low=0
        high=self.n-1
        while low<=high:
            mid=(low+high)//2
            if self.data[mid]<num:
                low=mid+1
            else:
                high=mid-1
        self.data.insert(low,num)
        self.n+=1

        

    def findMedian(self) -> float:
        if self.n%2==0:
            return (self.data[self.n//2-1]+self.data[self.n//2])/2
        return float(self.data[self.n//2])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()