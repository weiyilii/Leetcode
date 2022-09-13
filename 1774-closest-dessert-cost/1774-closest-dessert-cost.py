class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.res = float('inf')
        
        def dfs(cur, i):
            if abs(cur - target) < abs(self.res - target) or (abs(cur - target) == abs(self.res - target) and cur < self.res):
                self.res = cur
            if i >= len(toppingCosts) or cur >= target:
                return
            
            dfs(cur, i+1)
            dfs(cur + toppingCosts[i], i+1)
            dfs(cur + 2*toppingCosts[i], i+1)
        
        for base in baseCosts:
            dfs(base, 0)
        
        return self.res