class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            # ensure heights in stack is in acending order from bottom to top
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                res = max(res, height*width)
            stack.append(i)
        return res