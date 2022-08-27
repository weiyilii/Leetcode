class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        right_max = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            right_max = max(prices[i], right_max)
            res = max(res, right_max - prices[i])
        return res