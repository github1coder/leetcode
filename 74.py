class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m =len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r :
            mid=(r+l)//2 
            mid1=mid//n 
            mid2=mid%n 
            if matrix[mid1][mid2]>target:
                r=mid-1
            elif matrix[mid1][mid2]<target:
                l=mid+1
            else:
                return True
        return False