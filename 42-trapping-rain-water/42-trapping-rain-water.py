class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = len(height)
        left, right = [0]*l, [0]*l
        left_max, right_max = 0, 0
        for i in range(l):
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[l-1-i])
            left[i] = left_max
            right[l-1-i] = right_max
        for i in range(l):
            res += min(left[i], right[i]) - height[i]
        return res