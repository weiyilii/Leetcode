class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find dp[n]
        # 1 to n, each can be root
        # m as root
        # left has the number of dp[m] ways to get a BST
        # right has the number of dp[n-m-1] ways to get a BST
        # dp[m]*dp[n-m-1] ways to generate a full BST given m as root, n nodes in total
        # iterate m through 1 to n
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += (dp[j] * dp[i-j-1])
        return dp[n]