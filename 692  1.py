class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=collections.Counter(words)
        now=list(res.keys())
        now.sort(key= lambda i:(-res[i],i))
        return now[:k]