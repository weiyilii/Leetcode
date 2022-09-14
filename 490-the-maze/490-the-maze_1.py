class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # DFS
        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(i, j):
            if visited[i][j]:
                return False
            if i == destination[0] and j == destination[1]:
                return True
            visited[i][j] = True
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newi, newj = i, j
                while 0 <= newi + di < m and 0 <= newj + dj < n and maze[newi + di][newj + dj] == 0:
                    newi += di
                    newj += dj
                if dfs(newi, newj):
                    return True
            return False
        
        return dfs(start[0], start[1])
