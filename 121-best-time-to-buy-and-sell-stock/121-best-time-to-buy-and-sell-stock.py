class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = prices[:]
        res = 0
        for i in range(len(dp)-2, -1, -1):
            dp[i] = max(dp[i], dp[i+1])
            res = max(res, dp[i] - prices[i])
        return res