class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        upper = int(ceil((2*n + 0.25)**0.5 - 0.5)) + 1
        for m in range(1, upper):
            if (n - m*(m + 1)//2) % m == 0:
                res += 1
        return res