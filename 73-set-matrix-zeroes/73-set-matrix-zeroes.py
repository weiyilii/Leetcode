class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # extra variable to determine if first column should be changed to 0
        is_col = False 
        
        for i in range(m):
            # if any element in first column is 0, is_col = True
            if matrix[i][0] == 0:
                is_col = True
            # walk through all elements except those in first column
            for j in range(1, n):
                # if == 0, change the first cells in first column and row to 0
                # they will be flags to determine if changed to 0
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
                            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # if matrix[0][0] == 0, that means itself or any elements in first row is 0
        # first row should be changed to 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        # if is_col, first column should be changed to 0        
        if is_col:
            for i in range(m):
                matrix[i][0] = 0
        
        
        