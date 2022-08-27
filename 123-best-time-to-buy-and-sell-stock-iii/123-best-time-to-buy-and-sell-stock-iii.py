class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m, n = 3, len(prices)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for k in range(1, m):
            max_val = -prices[0]
            for i in range(1, n):
                max_val = max(max_val, dp[k-1][i-1] - prices[i])
                dp[k][i] = max(dp[k][i-1], prices[i] + max_val)
        return dp[-1][-1]