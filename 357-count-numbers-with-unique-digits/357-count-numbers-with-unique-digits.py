class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(1, n+1):
            num = 9
            for j in range(0, max(i-1, 0)):
                num = num*(9-j)
            res += num
        
        return res