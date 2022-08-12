class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # DFS
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'E':
                return
            # Check the number of mines in 8 neighbors
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] == 'M':
                        count += 1
            # If there are mines in 8 neighbors, update board with str(count), stop further search
            if count > 0:
                board[i][j] = str(count)
                return
            # If no mines in adjacent 8 grids, update board with 'B', continue search 8 neighbors
            else:
                board[i][j] = 'B'
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        dfs(i + di, j + dj)
        
        dfs(i, j)
        return board
