class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for m in range(1, n+1):
            l = len(res)
            for i in range(l-1, -1, -1):
                num = res[i] + 2**(m-1)
                res.append(num)
        return res