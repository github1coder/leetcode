class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        dic={}
        dic["]"],dic[")"],dic["}"]="[","(","{"
        stack=[]
        for a in s:
            if a not in dic:
                stack.append(a)
            else:
                if not stack or stack.pop()!=dic[a]:
                    return False
        if stack:
            return False
        return True