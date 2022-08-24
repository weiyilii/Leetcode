class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m, n = m-1, n-1
        denominator, divisor = 1, 1
        for i in range(n):
            denominator *= (m+n-i)
            divisor *= (n-i)
        return denominator/divisor