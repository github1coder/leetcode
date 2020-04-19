class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ss,ts=[],[]
        for s in S:
            if s!='#':
                ss.append(s)
            elif ss:
                ss.pop()
        for t in T :
            if t !='#':
                ts.append(t)
            elif ts:
                ts.pop()
        return ss==ts