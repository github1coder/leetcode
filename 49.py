class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for st in strs:
            li=list(st)
            li.sort()
            s="".join(li)
            if s in dic:
                dic[s]+=[st]
            else:
                dic[s]=[st]
        return [dic[item] for item in dic]