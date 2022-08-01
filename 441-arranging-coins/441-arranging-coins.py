class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left)//2
            if n >= mid*(mid + 1)/2 and n < (mid + 1)*(mid + 2)/2:
                return mid
            elif n >= (mid + 1)*(mid + 2)/2:
                left = mid + 1
            else:
                right = mid - 1