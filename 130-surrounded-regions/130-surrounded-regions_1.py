class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == "O":
                board[i][j] = "#"
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        for i in [0, m-1]:
            for j in range(n):
                dfs(i, j)   
        for j in [0, n-1]:
            for i in range(1, m-1):
                dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
