class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        height, width = 0, 0
        for i in range(len(horizontalCuts) - 1):
            height = max(height, horizontalCuts[i+1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            width = max(width, verticalCuts[i+1] - verticalCuts[i])
        return height*width%(10**9 + 7)