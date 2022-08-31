class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        
        if l < 3:
            return False
        
        mins = [0]*l
        mins[0] = nums[0]
        for i in range(1, l):
            mins[i] = min(mins[i-1], nums[i])
        stack = []
        for i in range(l-1, -1, -1):
            if stack and nums[i] > stack[-1]:
                while stack and nums[i] > stack[-1]:
                    n = stack.pop()
                    if n > mins[i]:
                        return True
            stack.append(nums[i])
        return False