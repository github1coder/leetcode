class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        for path in paths:
            doc=path.split(' ')
            for file in doc[1:]:
                name,content=file.split('(')
                d[content]+=[doc[0]+'/'+name]
        return filter(lambda s: len(s)>1,d.values())