class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Greedy
        # Scan twice: left -> right; right -> left
        # left -> right: keep count of left >= count of right, always expecting more right half will appear, otherwise reset two counters
        # right -> left, keep count of right >= count of left, always expecting more left half will appear, otherwise reset two counters
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
