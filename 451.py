class Solution:
    def frequencySort(self, s: str) -> str:
        cou=collections.Counter(s)
        now=sorted(cou.items(),key=lambda w:w[1],reverse=True)
        pr=[item[0]*int(cou[item[0]]) for item in now]
        re=''.join(pr)
        return re
