class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def dfs(i, j, char):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == "O":
                board[i][j] = char
                dfs(i-1, j, char)
                dfs(i+1, j, char)
                dfs(i, j-1, char)
                dfs(i, j+1, char)
        
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == "O":
                    dfs(i, j, "#")   
        for j in [0, n-1]:
            for i in range(1, m-1):
                if board[i][j] == "O":
                    dfs(i, j, "#")
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O":
                    dfs(i, j, "X")
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"