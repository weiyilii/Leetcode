class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for n in range(1, 10):
                            c = str(n)
                            if self.isValid(board, i, j, c):
                                board[i][j] = c
                                if solve():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        
        solve()
    
    def isValid(self, board, i, j, c):
        for k in range(9):
            if board[i][k] == c:
                return False
            if board[k][j] == c:
                return False
        x, y = (i//3)*3, (j//3)*3
        for m in range(x, x+3):
            for n in range(y, y+3):
                if board[m][n] == c:
                    return False
        return True