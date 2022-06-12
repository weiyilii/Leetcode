class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def checkrow(i):
            seen = {}
            for j in range(9):
                number = board[i][j]
                if number != ".":
                    if number in seen:
                        return False
                    else:
                        seen[number] = 1
            return True
        
        def checkcol(j):
            seen = {}
            for i in range(9):
                number = board[i][j]
                if number != ".":
                    if number in seen:
                        return False
                    else:
                        seen[number] = 1
            return True
        
        def checkbox(k):
            seen = {}
            start_i = 3*k%9
            start_j = 3*(k//3)
            for i in range(start_i, start_i+3):
                for j in range(start_j, start_j+3):
                    number = board[i][j]
                    if number != ".":
                        if number in seen:
                            return False
                        else:
                            seen[number] = 1
            return True
        
        for i in range(9):
            if not (checkrow(i) and checkcol(i) and checkbox(i)):
                return False
        return True