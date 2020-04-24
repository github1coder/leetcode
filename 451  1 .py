class Solution:
    def frequencySort(self, s: str) -> str:
        dic=collections.Counter(s)
        di=dic.most_common()
        st=[item[0]*int(item[1]) for item in di]
        return "".join(st)