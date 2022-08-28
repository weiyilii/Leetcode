class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = len(height)
        stack = []
        for i in range(l):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                pos = stack.pop()
                if not stack:
                    break
                h = min(height[stack[-1]], height[i]) - height[pos]
                w = i - stack[-1] - 1
                res += h*w
            stack.append(i)
        return res