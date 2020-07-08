class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s=0
        xor=x^y
        while xor:
            if xor&1:
                s+=1
            xor=xor>>1
        return s