class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        look=dic.most_common(k)
        return [item[0] for item in look]