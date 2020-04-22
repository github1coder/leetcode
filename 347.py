class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=collections.Counter(nums)
        now=res.most_common(k)
        no=[item[0] for item in now]
        return no