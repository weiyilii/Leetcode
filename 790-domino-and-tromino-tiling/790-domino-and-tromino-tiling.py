class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        f, p = [0]*n, [0]*n
        f[0], f[1] = 1, 2
        p[0], p[1] = 0, 2
        
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2] + p[i-1]
            p[i] = 2*f[i-2] + p[i-1]
        
        return f[-1] % (10**9 + 7)