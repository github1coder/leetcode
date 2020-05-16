class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for su in strs:
            s=sorted(list(su))
            s=''.join(s)
            if s in dic:
                dic[s].append(su)
            else:
                dic[s]=[su]
        return [dic[s] for s in dic]
