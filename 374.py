# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i=1
        j=n 
        while i<=j:
            mid=(i+j)//2
            t=guess(mid)
            if t ==-1:
                j=mid-1
            elif t==1:
                i=mid+1
            else:
                return mid