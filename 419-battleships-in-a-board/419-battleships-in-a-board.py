class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    res += 1
                    self.dfs(i, j, board)
        return res
    
    def dfs(self, i, j, board):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'X':
            board[i][j] = '.'
            self.dfs(i-1, j, board)
            self.dfs(i+1, j, board)
            self.dfs(i, j-1, board)
            self.dfs(i, j+1, board)