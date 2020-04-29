class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        def divide(left,up,right,down):
            if left>right or up>down:
                return False
            if target<matrix[up][left] or target>matrix[down][right]:
                return False
            mid=(left+right)//2
            row=up
            while row<=down and matrix[row][mid]<=target:
                if matrix[row][mid]==target:
                    return True
                row+=1
            return divide(left,row,mid-1,down) or divide(mid+1,up,right,row-1)
        return divide(0,0,len(matrix[0])-1,len(matrix)-1)