class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        left_max, right_max = [0]*l, [0]*l
        left, right, res = 0, 0, 0
        for i in range(l):
            left = max(left, height[i])
            right = max(right, height[l-i-1])
            left_max[i] = left
            right_max[l-i-1] = right
        for i in range(l):
            res += min(left_max[i], right_max[i]) - height[i]
        return res