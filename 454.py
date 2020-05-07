class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        num=0
        dic=collections.defaultdict(int)
        for a in A:
            for b in B:
                dic[a+b]+=1
        for c in C:
            for d in D:
                num+=dic[-c-d]
        return num