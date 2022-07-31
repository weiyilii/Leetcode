class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, digits = 1, 1
        while n > 9*start*digits:
            n -= 9*start*digits
            start = 10**digits
            digits += 1
        q, r = divmod(n-1, digits)
        res = str(start + q)[r]
        return res