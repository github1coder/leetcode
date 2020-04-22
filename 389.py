class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                del dic[i]
            else:
                dic[i]=1
        for i in t :
            if i in dic:
                del dic[i]
            else:
                dic[i]=1
        return list(dic)[0]