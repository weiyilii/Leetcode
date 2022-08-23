class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def dfs(path, left, right):
            if left == right == n:
                res.append(path)
                return
            if left > n or right > n:
                return
            
            if left == right:
                dfs(path + "(", left + 1, right)
            else:
                dfs(path + "(", left + 1, right)
                dfs(path + ")", left, right + 1)
        
        dfs("", 0, 0)
        return res