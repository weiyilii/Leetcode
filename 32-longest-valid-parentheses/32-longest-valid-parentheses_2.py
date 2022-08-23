class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Stack
        stack = [-1]
        res = 0
        # keep the stack top element is the index of element right previous to valid parentheses
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                # everytime meet ), pop stack
                # if stack becomes null, that means meet more ) than (, current i is invalid, append it to stack
                stack.pop()
                if not stack:
                    stack.append(i)
                # if stack not null, means till now, meet ( >= ), still valid, stack[-1] is the left element of the valid parenthese
                else:
                    res = max(res, i - stack[-1])
        return res
