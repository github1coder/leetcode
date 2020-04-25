class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        le1=len(haystack)
        le2=len(needle)
        i=0
        j=0
        while i<=le1-le2:
            if haystack[i]==needle[0]:
                while haystack[i+j]==needle[j]:
                    if j==le2-1:
                        return i 
                    j+=1
                j=0
            i+=1
        return -1