class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        self.nums.sort(reverse=True)
        self.le=len(self.nums)

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return self.nums[self.k-1]
        i=0
        j=self.le-1
        while i<=j:
            mid=(i+j)//2
            if self.nums[mid]<val:
                j=mid-1
            elif self.nums[mid]>val:
                i=mid+1
            else:
                self.nums.insert(mid,val)
                break
        if i>j:
            if i==0:
                if self.nums[i]>=val:
                    self.nums.insert(1,val)
                else :
                    self.nums.insert(0,val)
            elif j==self.le-1:
                if self.nums[j]<val:
                    self.nums.insert(j,val)
                else :
                    self.nums.append(val)
            else:
                if self.nums[i]>val:
                    self.nums.insert(j,val)
                else:
                    self.nums.insert(i,val)
        self.le+=1
        return self.nums[self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)