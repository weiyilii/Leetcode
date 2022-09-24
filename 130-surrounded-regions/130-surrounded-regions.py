class UF(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = 0
        
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        self.parent[rootp] = rootq
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        uf = UF(m*n + 1)
        dummy = m*n
        for i in range(m):
            if board[i][0] == "O":
                uf.union(i*n, dummy)
            if board[i][n-1] == "O":
                uf.union(i*n + n -1, dummy)
        for j in range(n):
            if board[0][j] == "O":
                uf.union(j, dummy)
            if board[m-1][j] == "O":
                uf.union(m*n-n+j, dummy)
                
        d = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O":
                    for k in range(4):
                        x, y = i + d[k][0], j + d[k][1]
                        if board[x][y] == "O":
                            uf.union(i*n+j, x*n+y)
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O" and not uf.connected(i*n+j, dummy):
                    board[i][j] = "X"