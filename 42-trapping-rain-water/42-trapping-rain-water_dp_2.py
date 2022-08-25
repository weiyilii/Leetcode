class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # DP idea with 2 pointers
        l = len(height)
        left_max, right_max = 0, 0
        left, right, res = 0, l - 1, 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # if height[left] < height[right]: area relies on left_max, update left
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res
