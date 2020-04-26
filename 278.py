# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        while i<n:
            mid=(i+n)//2
            if isBadVersion(mid):
                n=mid-1
            else:
                i=mid+1
        if isBadVersion(i):
            return i
        return i+1