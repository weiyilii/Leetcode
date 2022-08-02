class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        from math import log
        n = int(n)
        max_m = int(log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n**(m**(-1)))
            if n == (k**(m + 1) - 1)//(k - 1):
                return str(k)
        return str(n-1)