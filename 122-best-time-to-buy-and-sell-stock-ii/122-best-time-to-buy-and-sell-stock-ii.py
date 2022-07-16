class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        i, buy = 0, 0
        n = len(prices)
        
        while i < n:
            while i < n-1 and prices[i+1] > prices[i]:
                i += 1
            res += prices[i] - prices[buy]
            i += 1
            buy = i
        return res