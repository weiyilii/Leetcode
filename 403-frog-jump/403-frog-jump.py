class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        seen = set()
        
        def dfs(cur, step):
            if cur == target:
                return True
            if (cur, step) in seen:
                return False
            if step <= 0 or cur not in stones:
                return False
            for new in (step-1, step, step+1):
                if cur + new in stones and (cur + new, new) not in seen:
                    if dfs(cur+new, new):
                        return True
                    seen.add((cur+new, new))
        
        return dfs(1, 1)