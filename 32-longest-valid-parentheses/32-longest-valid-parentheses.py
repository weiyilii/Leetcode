class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        res = 0
        # keep the topmost element of the stack 
        # be the index of element right before each valid parentheses
        for i in range(len(s)):
            p = s[i]
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res