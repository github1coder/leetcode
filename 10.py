class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        les=len(s)
        lep=len(p)
        def match(indexs,indexp):
            if indexs==-1 and indexp==-1:
                return True
            if indexs==-1 and p[indexp]!='*':
                return False
            if indexp==-1:
                return False
            if indexs>=0 and (s[indexs]==p[indexp] or p[indexp]=='.'):
                return match(indexs-1,indexp-1)
            if p[indexp]=='*':
                if match(indexs,indexp-2):
                    return True
                for i in range(indexs,-2,-1):
                    if i==-1 or (s[i]!=p[indexp-1] and p[indexp-1]!='.'):
                        return match(i,indexp-2)
                    if match(i-1,indexp-2):
                        return True
                return False
            return False
        return match(les-1,lep-1)