class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=collections.Counter(words)
        now=list(res.keys())
        now.sort(key=lambda w:(-res[w],w))
        return now[:k]