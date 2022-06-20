class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 2 pointers
        # ensure there is a bar on the right which is higher than left_max
        # water can hold will only depend on left_max and height[left]
        left_max, right_max, res = 0, 0, 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                # worry: left_max too large?
                # as we have moved from left_max to left
                # this means sometime earlier when left=index(left_max),
                # we have seen height[index(left_max)] < height[right]
                # only then left pointer can be updated
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res