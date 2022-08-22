class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if sum(matchsticks) % 4 != 0:
            return False
        p = sum(matchsticks) / 4
        matchsticks.sort(reverse = True)
        sides = [0,0,0,0]
        l = len(matchsticks)
        
        def dfs(i):
            if i == l-1:
                if sides[0] == sides[1] == sides[3] == p:
                    return True
                return False
            for j in range(4):
                if sides[j] + matchsticks[i+1] <= p:
                    sides[j] += matchsticks[i+1]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i+1]
            return False
        
        return dfs(-1)