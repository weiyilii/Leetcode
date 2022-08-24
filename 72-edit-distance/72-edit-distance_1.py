class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # DP
        word1 = " " + word1
        word2 = " " + word2
        l1, l2 = len(word1), len(word2)
        # dp[i][j] = minimal number of operations needed to convert word1[:i+1] to word[:j+1]
        dp = [[0]*l2 for _ in range(l1)]
        for i in range(1, l1):
            dp[i][0] = i
        for j in range(1, l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j-1] + 1: replace word1[i] with word2[j]; dp[i][j-1] + 1: insert word2[j] to the index i of word1;
                    # dp[i-1][j] + 1: delete word1[i]
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[-1][-1]
