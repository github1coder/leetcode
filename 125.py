class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def small(c):
            if 'A'<=c<='Z':
                return chr(ord('a')+(ord(c)-ord('A')))
            return c 
        while i<j:
            while not('0'<=s[i]<='9' or 'a'<=small(s[i])<='z') and i<j :
                i+=1
            while not('0'<=s[j]<='9' or 'a'<=small(s[j])<='z') and i<j :
                j-=1
            if i<j:
                if small(s[i])!=small(s[j]):
                    return False
                else:
                    i+=1
                    j-=1
        return True