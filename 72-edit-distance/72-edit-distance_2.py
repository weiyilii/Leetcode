class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Recursion, more intuitive
        # TLE
        l1, l2 = len(word1), len(word2)
        def dfs(i, j):
            if i == l1 and j == l2:
                return 0
            if i == l1:
                return l2 - j
            if j == l2:
                return l1 - i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                # DP: base to final
                # recursion: final divide to base and return base to final
                insert = dfs(i, j+1) + 1
                delete = dfs(i+1, j) + 1
                replace = dfs(i+1, j+1) + 1
                return min(insert, delete, replace)
        return dfs(0, 0)
