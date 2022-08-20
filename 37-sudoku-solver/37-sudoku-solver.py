class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for n in range(1, 10):
                            c = str(n)
                            if self.isValid(board, i, j, c):
                                board[i][j] = c
                                if solve():
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True
        
        solve()
                                    
    
    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
        i, j = (row//3)*3, (col//3)*3
        for x in range(i, i+3):
            for y in range(j, j+3):
                if board[x][y] == c:
                    return False
        return True