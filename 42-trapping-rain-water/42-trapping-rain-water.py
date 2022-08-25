class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        for i in range(len(height)):
            while len(stack) > 0 and stack and height[i] > height[stack[-1]]:
                index = stack.pop()
                if not stack:
                    break
                h = min(height[i], height[stack[-1]]) - height[index]
                w = i - stack[-1] - 1
                res += h*w
            stack.append(i)
        return res