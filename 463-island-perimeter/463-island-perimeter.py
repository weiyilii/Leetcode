class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island, neighbor = 0, 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island += 1
                    if i < m-1 and grid[i+1][j] == 1:
                        neighbor += 1
                    if j < n-1 and grid[i][j+1] == 1:
                        neighbor += 1
        return 4*island - 2*neighbor