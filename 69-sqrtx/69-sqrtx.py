class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right - left)//2
            if mid*mid == x or (mid*mid < x and (mid+1)*(mid+1)) > x:
                return mid
            elif mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1