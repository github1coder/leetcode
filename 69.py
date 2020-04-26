class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        i=1
        j=x//2
        while i<j:
            mid=(i+j)//2
            num=mid*mid
            if num<x:
                i=mid+1
            elif num>x:
                j=mid-1
            else:
                return mid
        if i*i >x:
            return i-1
        return i 