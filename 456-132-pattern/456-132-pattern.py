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
                while stack and s1 > stack[-1]:
                    s3 = stack[-1]
                    stack.pop()
            stack.append(s1)
                    
        return False