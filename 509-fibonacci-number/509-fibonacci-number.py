class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        f0, f1 = 0, 1
        for i in range(2, n+1):
            f = f0 + f1
            f0 = f1
            f1 = f
        return f