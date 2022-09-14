class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # BFS
        from collections import deque
        m, n = len(maze), len(maze[0])
        q = deque([(start[0], start[1])])
        visited = [[False]*n for _ in range(m)]
        while q:
            i, j = q.popleft()
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newi, newj = i, j
                while 0 <= newi + di < m and 0 <= newj + dj < n and maze[newi + di][newj + dj] == 0:
                    newi += di
                    newj += dj
                if not visited[newi][newj]:
                    q.append((newi, newj))
                    visited[newi][newj] = True
        return False
