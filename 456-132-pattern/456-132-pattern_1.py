class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        s3 = float('-inf')
        for s1 in nums[::-1]:
            if s1 < s3:
                return True
            else:
                # Maintain a decreasing stack
                # Once a current element if less than stack top
                # Keep poping out s3 until current not > stack top (valid s2 > s3, current as s2)
                while stack and s1 > stack[-1]:
                    s3 = stack[-1]
                    stack.pop()
            stack.append(s1)
                    
        return False
