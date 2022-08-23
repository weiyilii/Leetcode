class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s < 4 or s % 4 != 0:
            return False
        matchsticks.sort(reverse = True)
        p = s // 4
        
        @cache # adding cache, saving some time
        def dfs(i, l1, l2, l3, l4):
            if i == len(matchsticks) - 1:
                if l1 == l2 == l3 == p:
                    return True
                return False
            if i > len(matchsticks) - 1:
                return False
            if l1 > p or l2 > p or l3 > p or l4 > p:
                return False
            return dfs(i+1, l1 + matchsticks[i+1], l2, l3, l4) or dfs(i+1, l1, l2 + matchsticks[i+1], l3, l4) or dfs(i+1, l1, l2, l3 + matchsticks[i+1], l4) or dfs(i+1, l1, l2, l3, l4 + matchsticks[i+1])
        
        return dfs(-1, 0, 0, 0, 0)
