class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        
        def dfs(cur):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                cur = cur*10 + i
                dfs(cur)
                cur = cur // 10
                        
        for i in range(1, min(10, n+1)):
            dfs(i)
            
        return res