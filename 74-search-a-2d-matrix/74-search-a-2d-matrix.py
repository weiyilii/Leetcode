class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        left_row, right_row = 0, m-1
        i = 0
        while left_row <= right_row:
            mid_row = left_row + (right_row - left_row)//2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                i = mid_row
                left_row = mid_row + 1
            else:
                right_row = mid_row - 1
        print(i)        
        left_col, right_col = 0, n-1
        while left_col <= right_col:
            mid_col = left_col + (right_col - left_col)//2
            if matrix[i][mid_col] == target:
                return True
            elif matrix[i][mid_col] < target:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1
        
        return False