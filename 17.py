class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        le=len(digits)
        def back(path,index):
            if index>=le:
                res.append(path)
                return 
            if '2'<=digits[index]<='6':
                t=ord('a')+(int(digits[index])-2)*3
                for s in [chr(t),chr(t+1),chr(t+2)]:
                    back(path+s,index+1)
            else:
                if digits[index]=='7':
                    for s in ['p','q','r','s']:
                        back(path+s,index+1)
                elif digits[index]=='8':
                    for s in ['t','u','v']:
                        back(path+s,index+1)
                elif digits[index]=='9':
                    for s in ['w','x','y','z']:
                        back(path+s,index+1)
        back('',0)
        return res