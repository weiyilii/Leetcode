class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(0, int(sqrt(c)) + 1):
            target = c - a*a
            left, right = a, c
            while left <= right:
                mid = left + (right - left) // 2
                if mid * mid == target:
                    return True
                elif mid * mid < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False