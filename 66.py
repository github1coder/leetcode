class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        le=len(digits)
        n=le-1
        sign=1
        while sign!=0 and n>=0:
            if digits[n]+sign>=10:
                digits[n]=0
                n-=1
                sign=1
            else:
                digits[n]+=1
                sign=0
        if n<0:
            digits.insert(0,1)
        return digits