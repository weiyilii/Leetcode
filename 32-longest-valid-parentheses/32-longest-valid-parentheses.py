class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        l = len(s)
        res = 0
        for i in range(l):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left + right)
            if right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(l-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left + right)
            if left > right:
                left, right = 0, 0
        return res