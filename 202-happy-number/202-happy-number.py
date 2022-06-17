class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        cur = n
        while cur not in seen:
            seen.add(cur)
            new = 0
            for i in str(cur):
                new += int(i)**2
            cur = new
            if cur == 1:
                return True
        return False