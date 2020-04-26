class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)-1
        if m==-1:
            return False
        n=len(matrix[0])-1
        dui=0
        while dui<=m and dui<=n :
            l=dui
            r=n
            while l<=r:
                mid=(l+r)//2
                if matrix[dui][mid]<target:
                    l=mid+1
                elif matrix[dui][mid]>target:
                    r=mid-1
                else:
                    return True
            l =dui
            r =m 
            while l<=r:
                mid=(l+r)//2
                if matrix[mid][dui]<target:
                    l=mid+1
                elif matrix[mid][dui]>target:
                    r=mid-1
                else:
                    return True
            dui+=1
        return False