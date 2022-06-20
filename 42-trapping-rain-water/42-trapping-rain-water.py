class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, cur = 0, 0
        stack = []
        
        while cur < len(height):
            while len(stack) > 0 and height[cur] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = cur - stack[-1] - 1
                bounded_height = min(height[cur], height[stack[-1]]) - height[top]
                res += distance*bounded_height
            stack.append(cur)
            cur += 1
        
        return res