class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Use memorization
        cache = {}
        
        def dfs(s1, s2):
            l = len(s1)
            if (s1, s2) in cache:
                return cache[(s1, s2)]
            if sorted(s1) != sorted(s2):
                cache[(s1, s2)] = False
                return False
            if s1 == s2:
                cache[(s1, s2)] = True
                return True
            for i in range(1, l):
                if (dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])) or (dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i])):
                    cache[(s1, s2)] = True
                    return True
            cache[(s1, s2)] = False
            return False
        
        return dfs(s1, s2)
                
