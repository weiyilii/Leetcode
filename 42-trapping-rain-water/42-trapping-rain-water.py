class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_max, right_max = [0]*n, [0]*n
        left, right, res = 0, 0, 0
        for i in range(n):
            left_max[i] = max(left, height[i])
            right_max[n-i-1] = max(right, height[n-i-1])
            left, right = left_max[i], right_max[n-i-1]
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res