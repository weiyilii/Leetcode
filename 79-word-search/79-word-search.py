class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(i, j, seen, k):
            if k == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen or board[i][j] != word[k]:
                return False
            
            seen.add((i, j))
            
            res = (search(i-1, j, seen, k+1) or
                   search(i+1, j, seen, k+1) or
                   search(i, j-1, seen, k+1) or
                   search(i, j+1, seen, k+1)) 
            seen.remove((i, j))
            return res
                    
        m, n, l = len(board), len(board[0]), len(word)
        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j, set(), 0):
                        return True
        return False