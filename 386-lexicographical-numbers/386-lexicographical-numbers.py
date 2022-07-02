class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(cur, res):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                cur = cur*10 + i
                dfs(cur, res)
                cur = cur // 10
                
        res = []
        for i in range(1, min(10, n+1)):
            dfs(i, res)
        return res