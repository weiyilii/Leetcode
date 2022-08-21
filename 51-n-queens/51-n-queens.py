class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        
        def dfs(q):
            i = len(q)
            if i == n:
                board = []
                for k in range(n):
                    row = ""
                    for v in range(n):
                        if v == q[k][1]:
                            row += "Q"
                        else:
                            row += "."
                    board.append(row)
                res.append(board)
                return
            for j in range(n):
                if self.isValid(q, i, j):
                    q.append([i, j])
                    dfs(q)
                    q.pop()
        
        dfs([])
        return res
    
    def isValid(self, q, i, j):
        for x, y in q:
            if x + y == i + j or x - y == i - j or y == j:
                return False
        return True