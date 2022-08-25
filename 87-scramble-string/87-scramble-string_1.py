class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        # Recursive dfs
        @cache
        def dfs(s1, s2):
            l = len(s1)
            # make sure s1 and s2 contain same counts of same letters, else False
            if sorted(s1) != sorted(s2):
                return False
            # if l < 4 like "abc", all the permutations are scrambles of each other
            if l < 4 or s1 == s2:
                return True
            for i in range(1, l):
                if (dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])) or (dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i])):
                    return True
            return False
        
        return dfs(s1, s2)
                
