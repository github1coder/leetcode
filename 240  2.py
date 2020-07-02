class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        if n==0:
            return False
        m=len(matrix[0])
        i=n-1
        j=0
        while 0<=i<=n-1 and 0<=j<=m-1:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                i-=1
            else:
                j+=1
        return False
