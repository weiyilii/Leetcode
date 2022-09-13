class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # Brute Force
        res = []
        for base in baseCosts:
            res.append(base)
        for topping in toppingCosts:
            l = len(res)
            for i in range(l):
                for j in [1, 2]:
                    res.append(res[i] + j*topping)
                    
        res.sort(key = lambda x: (abs(x - target), x))
        return res[0]
        
